from __future__ import annotations

from typing import Any

from .ai import (AgentRuntime, Assistant, DocumentProcessor, ExpertSystem,
                 ModelPlatform, NLP, RecommendationEngine, VectorStore, Vision)
from .ai.agents import AgentTool
from .analytics import AnalyticsEngine
from .catalog import Catalog
from .governance import Governance
from .mdm import MasterDataManager
from .models import DataAsset, PipelineDefinition, QualityRule, new_id, utc_now
from .observability import Observability
from .pipeline import PipelineEngine
from .quality import QualityEngine
from .registry import discover
from .storage import Storage
from .streaming import EventProcessor


class DataIntelligencePlatform:
    def __init__(self, database: str | None = None):
        self.storage = Storage(database)
        self.catalog = Catalog(self.storage)
        self.quality = QualityEngine(self.storage)
        self.pipelines = PipelineEngine(self.storage)
        self.analytics = AnalyticsEngine()
        self.streaming = EventProcessor(self.storage)
        self.mdm = MasterDataManager(self.storage)
        self.governance = Governance(self.storage)
        self.observability = Observability(self.storage)
        self.vectors = VectorStore(self.storage)
        self.models = ModelPlatform(self.storage)
        self.nlp = NLP()
        self.documents = DocumentProcessor(self.nlp)
        self.recommendations = RecommendationEngine()
        self.vision = Vision()
        self.expert = ExpertSystem()
        self.assistant = Assistant(self.storage, self.vectors)
        self.agents = AgentRuntime()
        self._register_agent_tools()
        self.streaming.add_rule("High-value event burst", lambda events: sum(float(e["payload"].get("value", 0)) for e in events[-10:]) > 10000, "critical")

    def _register_agent_tools(self) -> None:
        self.agents.register(AgentTool(
            "vector_search", "Search grounded enterprise knowledge",
            lambda args: self.vectors.search(args["collection"], args["query"], int(args.get("limit", 5))),
            ("collection", "query"),
        ))
        self.agents.register(AgentTool(
            "model_predict", "Run an active model deployment",
            lambda args: self.models.predict(args["model"], args["rows"], args.get("environment", "production")),
            ("model", "rows"),
        ))
        self.agents.register(AgentTool(
            "catalog_search", "Search governed data assets",
            lambda args: self.catalog.list(args.get("query", ""), args.get("domain", "")),
        ))
        self.agents.register(AgentTool(
            "nlp_analyze", "Analyze sentiment, entities, keywords and language",
            lambda args: self.nlp.analyze(args["text"]), ("text",),
        ))

    def ingest(self, name: str, domain: str, owner: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
        schema = {field: type(value).__name__ for row in rows[:20] for field, value in row.items()}
        existing = next((asset for asset in self.catalog.list() if asset["name"] == name), None)
        if existing:
            asset_id = existing["id"]
        else:
            asset_id = self.catalog.register(DataAsset(name, domain, owner, f"Managed dataset {name}", schema=schema, tags=[domain]))["id"]
        current = self.storage.one("SELECT COALESCE(MAX(version),0) AS version FROM datasets WHERE asset_id=?", (asset_id,))["version"]
        dataset_id, created = new_id("dsv"), utc_now()
        self.storage.execute("INSERT INTO datasets VALUES (?,?,?,?,?,?)", (dataset_id, asset_id, current + 1, len(rows), self.storage.encode(rows), created))
        self.governance.audit(owner, "ingest", asset_id, {"rows": len(rows), "version": current + 1})
        self.observability.record("ingested_rows", len(rows), {"asset": name})
        return {"dataset_id": dataset_id, "asset_id": asset_id, "version": current + 1, "rows": len(rows)}

    def dataset(self, asset_id: str) -> list[dict[str, Any]]:
        record = self.storage.one("SELECT rows_json FROM datasets WHERE asset_id=? ORDER BY version DESC LIMIT 1", (asset_id,))
        return self.storage.decode(record["rows_json"]) if record else []

    def overview(self) -> dict[str, Any]:
        health = self.observability.health()
        quality = self.storage.one("SELECT AVG(score) AS score FROM quality_results")
        jobs = self.storage.query("SELECT * FROM jobs ORDER BY started_at DESC LIMIT 8")
        model_count = self.storage.one("SELECT COUNT(*) AS count FROM ai_models")["count"]
        vector_count = self.storage.one("SELECT COUNT(*) AS count FROM vector_documents")["count"]
        return {"health": health, "quality_score": round(quality["score"] or 1, 4),
                "capabilities": len(discover()), "families": len({c.family for c in discover().values()}),
                "ai": {"models": model_count, "vector_documents": vector_count,
                       "agent_tools": len(self.agents.tools)},
                "assets": self.catalog.list(), "recent_jobs": jobs,
                "recommendations": self.analytics.recommend({"quality_score": quality["score"] or 1, "pipeline_failures": health["failed_jobs"]})}

    def seed_demo(self) -> dict[str, Any]:
        rows = [
            {"id": 1, "region": "South", "product": "Lakehouse", "revenue": 12500.0, "email": "ana@example.com"},
            {"id": 2, "region": "Southeast", "product": "BI", "revenue": 18000.0, "email": "rui@example.com"},
            {"id": 3, "region": "South", "product": "Governance", "revenue": 9200.0, "email": "bia@example.com"},
            {"id": 4, "region": "Northeast", "product": "Analytics", "revenue": 14300.0, "email": "leo@example.com"},
        ]
        ingestion = self.ingest("sales_demo", "commercial", "demo-steward", rows)
        rules = [QualityRule("Identifier required", "required", "id"), QualityRule("Revenue nonnegative", "minimum", "revenue", 0)]
        quality = self.quality.run(ingestion["asset_id"], rows, rules)
        cube = self.analytics.aggregate(rows, ["region"], "revenue", "sum").to_dict()
        for row in rows:
            self.streaming.publish("sales", "sale.recorded", {"value": row["revenue"], "region": row["region"]})
        return {"ingestion": ingestion, "quality": quality, "cube": cube, "overview": self.overview()}

    def seed_ai_demo(self) -> dict[str, Any]:
        training = [
            {"sessions": 2, "spend": 40, "churned": "yes"},
            {"sessions": 18, "spend": 920, "churned": "no"},
            {"sessions": 4, "spend": 80, "churned": "yes"},
            {"sessions": 12, "spend": 640, "churned": "no"},
            {"sessions": 3, "spend": 55, "churned": "yes"},
            {"sessions": 16, "spend": 790, "churned": "no"},
        ]
        model = self.models.train("customer_churn", "binary_classification", training,
                                  ["sessions", "spend"], "churned", "demo-ml-engineer",
                                  "Customer churn propensity")
        deployment = self.models.deploy("customer_churn")
        prediction = self.models.predict("customer_churn", [{"sessions": 5, "spend": 120}])
        documents = [
            ("retention-policy", "Clientes com baixo engajamento recebem uma oferta de retencao personalizada."),
            ("privacy-policy", "Dados pessoais devem ser minimizados, criptografados e auditados."),
        ]
        for identifier, text in documents:
            self.vectors.upsert("knowledge", text, {"kind": "policy"}, identifier)
        answer = self.assistant.ask("O que fazer com clientes de baixo engajamento?")
        return {"model": model, "deployment": deployment, "prediction": prediction,
                "assistant": answer, "overview": self.overview()}
