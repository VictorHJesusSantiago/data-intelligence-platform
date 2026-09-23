from __future__ import annotations

from typing import Any

from .models import PipelineDefinition, new_id, utc_now
from .registry import execute
from .storage import Storage


class PipelineEngine:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save(self, pipeline: PipelineDefinition) -> dict[str, Any]:
        self.storage.execute("INSERT OR REPLACE INTO pipelines VALUES (?,?,?,?,?)",
            (pipeline.id, pipeline.name, self.storage.encode(pipeline.to_dict()), 1, utc_now()))
        return pipeline.to_dict()

    def run(self, pipeline: PipelineDefinition, rows: list[dict[str, Any]]) -> dict[str, Any]:
        job_id, started, current, traces = new_id("job"), utc_now(), rows, []
        self.storage.execute("INSERT INTO jobs(id,pipeline_id,status,input_rows,started_at) VALUES(?,?,?,?,?)",
                             (job_id, pipeline.id, "running", len(rows), started))
        try:
            for step in pipeline.steps:
                before = len(current) if isinstance(current, list) else 1
                current = execute(step["capability"], current, step.get("configuration"))
                after = len(current) if isinstance(current, list) else 1
                traces.append({"capability": step["capability"], "before": before, "after": after})
            output_rows = len(current) if isinstance(current, list) else 1
            self.storage.execute("UPDATE jobs SET status=?,output_rows=?,details_json=?,finished_at=? WHERE id=?",
                                 ("succeeded", output_rows, self.storage.encode(traces), utc_now(), job_id))
            return {"job_id": job_id, "status": "succeeded", "data": current, "trace": traces}
        except Exception as exc:
            self.storage.execute("UPDATE jobs SET status=?,details_json=?,finished_at=? WHERE id=?",
                                 ("failed", self.storage.encode({"error": str(exc), "trace": traces}), utc_now(), job_id))
            raise
