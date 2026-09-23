from __future__ import annotations

import argparse
import json
from pathlib import Path

from .api import serve
from .registry import discover
from .service import DataIntelligencePlatform


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="dip", description="Data Intelligence Platform")
    root.add_argument("--database", help="SQLite database path")
    commands = root.add_subparsers(dest="command", required=True)
    web = commands.add_parser("serve", help="Run API and BI portal")
    web.add_argument("--host", default="127.0.0.1")
    web.add_argument("--port", type=int, default=8080)
    commands.add_parser("demo", help="Load a complete demonstration dataset")
    commands.add_parser("ai-demo", help="Run the local AI/ML end-to-end demonstration")
    commands.add_parser("status", help="Print platform health and KPIs")
    commands.add_parser("validate", help="Import and exercise every capability")
    ingest = commands.add_parser("ingest", help="Ingest a JSON array")
    ingest.add_argument("file", type=Path)
    ingest.add_argument("--name", required=True)
    ingest.add_argument("--domain", default="default")
    ingest.add_argument("--owner", default="cli")
    ask = commands.add_parser("ask", help="Ask the grounded AI assistant")
    ask.add_argument("question")
    ask.add_argument("--collection", default="knowledge")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    platform = DataIntelligencePlatform(args.database)
    if args.command == "serve":
        serve(platform, args.host, args.port)
        return 0
    if args.command == "demo":
        result = platform.seed_demo()
    elif args.command == "ai-demo":
        result = platform.seed_ai_demo()
    elif args.command == "ask":
        result = platform.assistant.ask(args.question, args.collection)
    elif args.command == "status":
        result = platform.overview()
    elif args.command == "ingest":
        rows = json.loads(args.file.read_text(encoding="utf-8"))
        if not isinstance(rows, list):
            raise SystemExit("input must be a JSON array")
        result = platform.ingest(args.name, args.domain, args.owner, rows)
    else:
        sample = [{"id": 1, "value": 10.0, "region": "south", "email": "a@b.com"},
                  {"id": 2, "value": 20.0, "region": "north", "email": "c@d.com"}]
        failures = []
        for code, capability in discover().items():
            try: capability.execute(sample)
            except Exception as exc: failures.append({"code": code, "error": str(exc)})
        result = {"capabilities": len(discover()), "failures": failures, "valid": not failures}
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if not result.get("failures") else 1
