"""Orchestration Control 23: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.23",
    family="orchestration",
    title='Orchestration Control 23',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="project",
    configuration={'field': 'source', 'target': 'orchestration_value_23', 'fields': ['id', 'source', 'value']},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
