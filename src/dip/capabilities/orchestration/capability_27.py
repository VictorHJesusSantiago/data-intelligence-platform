"""Orchestration Control 27: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.27",
    family="orchestration",
    title='Orchestration Control 27',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="dedupe",
    configuration={'field': 'email', 'target': 'orchestration_value_27'},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
