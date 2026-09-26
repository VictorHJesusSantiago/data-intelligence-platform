"""Orchestration Control 13: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.13",
    family="orchestration",
    title='Orchestration Control 13',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="project",
    configuration={'field': 'source', 'target': 'orchestration_value_13', 'fields': ['id', 'source', 'value']},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
