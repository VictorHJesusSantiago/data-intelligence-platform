"""Orchestration Control 02: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.02",
    family="orchestration",
    title='Orchestration Control 02',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="filter_not_null",
    configuration={'field': 'amount', 'target': 'orchestration_value_02'},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
