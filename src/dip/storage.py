from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator


SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS assets (
 id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, domain TEXT NOT NULL,
 owner TEXT NOT NULL, description TEXT NOT NULL, classification TEXT NOT NULL,
 schema_json TEXT NOT NULL, tags_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS datasets (
 id TEXT PRIMARY KEY, asset_id TEXT NOT NULL REFERENCES assets(id),
 version INTEGER NOT NULL, row_count INTEGER NOT NULL, rows_json TEXT NOT NULL,
 created_at TEXT NOT NULL, UNIQUE(asset_id, version)
);
CREATE TABLE IF NOT EXISTS pipelines (
 id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, definition_json TEXT NOT NULL,
 enabled INTEGER NOT NULL DEFAULT 1, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS jobs (
 id TEXT PRIMARY KEY, pipeline_id TEXT, status TEXT NOT NULL,
 input_rows INTEGER NOT NULL DEFAULT 0, output_rows INTEGER NOT NULL DEFAULT 0,
 details_json TEXT NOT NULL DEFAULT '{}', started_at TEXT NOT NULL, finished_at TEXT
);
CREATE TABLE IF NOT EXISTS quality_results (
 id TEXT PRIMARY KEY, asset_id TEXT NOT NULL, score REAL NOT NULL,
 passed INTEGER NOT NULL, results_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS lineage_edges (
 id TEXT PRIMARY KEY, source_asset TEXT NOT NULL, target_asset TEXT NOT NULL,
 operation TEXT NOT NULL, job_id TEXT, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS master_records (
 id TEXT PRIMARY KEY, entity_type TEXT NOT NULL, natural_key TEXT NOT NULL,
 golden_json TEXT NOT NULL, source_count INTEGER NOT NULL, updated_at TEXT NOT NULL,
 UNIQUE(entity_type, natural_key)
);
CREATE TABLE IF NOT EXISTS events (
 id TEXT PRIMARY KEY, topic TEXT NOT NULL, event_type TEXT NOT NULL,
 payload_json TEXT NOT NULL, event_time TEXT NOT NULL, processed INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS alerts (
 id TEXT PRIMARY KEY, severity TEXT NOT NULL, title TEXT NOT NULL,
 message TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS metrics (
 name TEXT NOT NULL, value REAL NOT NULL, labels_json TEXT NOT NULL,
 recorded_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS audit_log (
 id INTEGER PRIMARY KEY AUTOINCREMENT, actor TEXT NOT NULL, action TEXT NOT NULL,
 resource TEXT NOT NULL, details_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ai_models (
 id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, task TEXT NOT NULL,
 description TEXT NOT NULL, owner TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ai_model_versions (
 id TEXT PRIMARY KEY, model_id TEXT NOT NULL REFERENCES ai_models(id),
 version INTEGER NOT NULL, algorithm TEXT NOT NULL, artifact_json TEXT NOT NULL,
 metrics_json TEXT NOT NULL, training_rows INTEGER NOT NULL, created_at TEXT NOT NULL,
 UNIQUE(model_id, version)
);
CREATE TABLE IF NOT EXISTS ai_deployments (
 id TEXT PRIMARY KEY, model_id TEXT NOT NULL REFERENCES ai_models(id),
 version INTEGER NOT NULL, environment TEXT NOT NULL, status TEXT NOT NULL,
 traffic REAL NOT NULL, created_at TEXT NOT NULL,
 UNIQUE(model_id, environment)
);
CREATE TABLE IF NOT EXISTS ai_predictions (
 id TEXT PRIMARY KEY, model_id TEXT NOT NULL, version INTEGER NOT NULL,
 input_json TEXT NOT NULL, output_json TEXT NOT NULL, latency_ms REAL NOT NULL,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS vector_documents (
 id TEXT PRIMARY KEY, collection TEXT NOT NULL, text TEXT NOT NULL,
 metadata_json TEXT NOT NULL, vector_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_vector_documents_collection
 ON vector_documents(collection);
CREATE TABLE IF NOT EXISTS ai_conversations (
 id TEXT PRIMARY KEY, title TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ai_messages (
 id TEXT PRIMARY KEY, conversation_id TEXT NOT NULL REFERENCES ai_conversations(id),
 role TEXT NOT NULL, content TEXT NOT NULL, context_json TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_ai_messages_conversation
 ON ai_messages(conversation_id, created_at);
"""


class Storage:
    def __init__(self, path: str | Path | None = None):
        base = Path(os.getenv("DIP_DATA_DIR", "var"))
        base.mkdir(parents=True, exist_ok=True)
        self.path = str(path or base / "platform.db")
        self.initialize()

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(SCHEMA)

    def execute(self, sql: str, params: tuple[Any, ...] = ()) -> int:
        with self.connect() as connection:
            cursor = connection.execute(sql, params)
            return cursor.rowcount

    def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        with self.connect() as connection:
            return [dict(row) for row in connection.execute(sql, params).fetchall()]

    def one(self, sql: str, params: tuple[Any, ...] = ()) -> dict[str, Any] | None:
        rows = self.query(sql, params)
        return rows[0] if rows else None

    @staticmethod
    def encode(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)

    @staticmethod
    def decode(value: str) -> Any:
        return json.loads(value)
