from __future__ import annotations

import base64
import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .errors import AuthorizationError, PlatformError
from .registry import discover
from .security import authenticate
from .service import DataIntelligencePlatform


WEB = Path(__file__).with_name("web")


class APIHandler(BaseHTTPRequestHandler):
    platform: DataIntelligencePlatform

    def _json(self, status: int, payload: object) -> None:
        body = json.dumps(payload, ensure_ascii=False, default=str).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self'; script-src 'self'")
        self.end_headers()
        self.wfile.write(body)

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length) or b"{}")

    def _principal(self, permission: str):
        principal = authenticate(self.headers.get("X-API-Key"))
        principal.require(permission)
        return principal

    def do_GET(self) -> None:
        try:
            parsed = urlparse(self.path)
            if parsed.path in {"/", "/index.html"}:
                return self._file("index.html")
            if parsed.path.startswith("/assets/"):
                return self._file(parsed.path.removeprefix("/assets/"))
            if parsed.path == "/api/health":
                return self._json(200, self.platform.observability.health())
            self._principal("read")
            if parsed.path == "/api/overview":
                return self._json(200, self.platform.overview())
            if parsed.path == "/api/assets":
                query = parse_qs(parsed.query)
                return self._json(200, self.platform.catalog.list(query.get("q", [""])[0], query.get("domain", [""])[0]))
            if parsed.path == "/api/lineage":
                return self._json(200, self.platform.catalog.lineage())
            if parsed.path == "/api/capabilities":
                return self._json(200, [cap.to_dict() for cap in discover().values()])
            if parsed.path == "/api/ai/models":
                return self._json(200, self.platform.models.list())
            if parsed.path == "/api/ai/vector/collections":
                return self._json(200, self.platform.vectors.collections())
            if parsed.path == "/api/ai/agent/tools":
                return self._json(200, self.platform.agents.catalog())
            if parsed.path == "/api/ai/conversations/history":
                query = parse_qs(parsed.query)
                return self._json(200, self.platform.assistant.history(query["id"][0]))
            self._json(404, {"error": "not_found"})
        except AuthorizationError as exc:
            self._json(401, {"error": str(exc)})
        except (PlatformError, ValueError) as exc:
            self._json(400, {"error": str(exc)})

    def do_POST(self) -> None:
        try:
            principal = self._principal("write")
            if self.path == "/api/ingest":
                body = self._body()
                result = self.platform.ingest(body["name"], body.get("domain", "default"), principal.name, body["rows"])
                return self._json(201, result)
            if self.path == "/api/demo":
                return self._json(201, self.platform.seed_demo())
            if self.path == "/api/ai/demo":
                return self._json(201, self.platform.seed_ai_demo())
            if self.path == "/api/query":
                body = self._body()
                rows = self.platform.dataset(body["asset_id"])
                result = self.platform.analytics.aggregate(rows, body.get("dimensions", []), body["measure"], body.get("operation", "sum"))
                return self._json(200, result.to_dict())
            if self.path == "/api/ai/vector/upsert":
                body = self._body()
                return self._json(201, self.platform.vectors.upsert(
                    body["collection"], body["text"], body.get("metadata"), body.get("id")
                ))
            if self.path == "/api/ai/vector/search":
                body = self._body()
                return self._json(200, self.platform.vectors.search(
                    body["collection"], body["query"], int(body.get("limit", 5)), body.get("filters")
                ))
            if self.path == "/api/ai/chat":
                body = self._body()
                return self._json(200, self.platform.assistant.ask(
                    body["question"], body.get("collection", "knowledge"),
                    body.get("conversation_id"), int(body.get("limit", 5))
                ))
            if self.path == "/api/ai/train":
                body = self._body()
                return self._json(201, self.platform.models.train(
                    body["name"], body["task"], body["rows"], body["features"], body.get("target"),
                    principal.name, body.get("description", ""), int(body.get("clusters", 3))
                ))
            if self.path == "/api/ai/automl":
                body = self._body()
                return self._json(201, self.platform.models.automl(
                    body["name"], body["rows"], body["target"], principal.name,
                    body.get("description", "")
                ))
            if self.path == "/api/ai/deploy":
                body = self._body()
                return self._json(201, self.platform.models.deploy(
                    body["name"], body.get("version"), body.get("environment", "production"),
                    float(body.get("traffic", 1.0))
                ))
            if self.path == "/api/ai/predict":
                body = self._body()
                return self._json(200, self.platform.models.predict(
                    body["name"], body["rows"], body.get("environment", "production"), body.get("version")
                ))
            if self.path == "/api/ai/drift":
                body = self._body()
                return self._json(200, self.platform.models.drift(body["name"], body["rows"], body.get("version")))
            if self.path == "/api/ai/nlp":
                body = self._body()
                return self._json(200, self.platform.nlp.analyze(body["text"], body.get("labels")))
            if self.path == "/api/ai/document":
                body = self._body()
                return self._json(200, self.platform.documents.process(
                    body["content"], body.get("media_type", "text/plain"), body.get("fields")
                ))
            if self.path == "/api/ai/vision/analyze":
                body = self._body()
                return self._json(200, self.platform.vision.analyze_pgm(
                    base64.b64decode(body["image_base64"], validate=True), body.get("threshold")
                ))
            if self.path == "/api/ai/recommend":
                body = self._body()
                return self._json(200, self.platform.recommendations.rank(
                    body["items"], body.get("profile", {}), int(body.get("limit", 10)), body.get("interactions")
                ))
            if self.path == "/api/ai/agent/run":
                body = self._body()
                return self._json(200, self.platform.agents.run(body["goal"], body["steps"]))
            if self.path == "/api/ai/expert/evaluate":
                body = self._body()
                return self._json(200, self.platform.expert.evaluate(body.get("facts", {}), body["rules"]))
            self._json(404, {"error": "not_found"})
        except AuthorizationError as exc:
            self._json(401, {"error": str(exc)})
        except (KeyError, PlatformError, ValueError) as exc:
            self._json(400, {"error": str(exc)})

    def _file(self, name: str) -> None:
        path = (WEB / name).resolve()
        if WEB.resolve() not in path.parents and path != WEB.resolve():
            return self._json(403, {"error": "forbidden"})
        if not path.is_file():
            return self._json(404, {"error": "not_found"})
        body = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mimetypes.guess_type(path.name)[0] or "application/octet-stream")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        return


def serve(platform: DataIntelligencePlatform, host: str = "127.0.0.1", port: int = 8080) -> None:
    APIHandler.platform = platform
    server = ThreadingHTTPServer((host, port), APIHandler)
    print(f"Data Intelligence Platform listening at http://{host}:{port}")
    server.serve_forever()
