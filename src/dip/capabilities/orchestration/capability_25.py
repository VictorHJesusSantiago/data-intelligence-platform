"""Orchestration Control 25: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.25",
    family="orchestration",
    title='Orchestration Control 25',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="aggregate",
    configuration={'field': 'value', 'target': 'orchestration_value_25'},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
