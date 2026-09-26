"""Orchestration Control 12: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.12",
    family="orchestration",
    title='Orchestration Control 12',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="filter_not_null",
    configuration={'field': 'amount', 'target': 'orchestration_value_12'},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
