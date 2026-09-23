from __future__ import annotations

from collections import defaultdict, deque
from datetime import datetime, timezone
from typing import Any, Callable

from .models import new_id, utc_now
from .storage import Storage


class EventProcessor:
    def __init__(self, storage: Storage, window_size: int = 100):
        self.storage, self.window_size = storage, window_size
        self.windows: dict[str, deque] = defaultdict(lambda: deque(maxlen=window_size))
        self.rules: list[tuple[str, Callable[[list[dict]], bool], str]] = []

    def add_rule(self, name: str, predicate: Callable[[list[dict]], bool], severity: str = "warning") -> None:
        self.rules.append((name, predicate, severity))

    def publish(self, topic: str, event_type: str, payload: dict[str, Any]) -> dict[str, Any]:
        event = {"id": new_id("evt"), "topic": topic, "event_type": event_type,
                 "payload": payload, "event_time": datetime.now(timezone.utc).isoformat()}
        self.storage.execute("INSERT INTO events VALUES (?,?,?,?,?,?)", (event["id"], topic, event_type,
                             self.storage.encode(payload), event["event_time"], 1))
        self.windows[topic].append(event)
        alerts = []
        snapshot = list(self.windows[topic])
        for name, predicate, severity in self.rules:
            if predicate(snapshot):
                alert = {"id": new_id("alt"), "severity": severity, "title": name,
                         "message": f"CEP rule matched on {topic}", "status": "open", "created_at": utc_now()}
                self.storage.execute("INSERT INTO alerts VALUES (?,?,?,?,?,?)", tuple(alert.values()))
                alerts.append(alert)
        return {"event": event, "alerts": alerts}
