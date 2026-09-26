"""Orchestration Control 04: Schedules, dependencies, retries and backfill coordination."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="orchestration.04",
    family="orchestration",
    title='Orchestration Control 04',
    description='Schedules, dependencies, retries and backfill coordination',
    operation="derive",
    configuration={'field': 'id', 'target': 'orchestration_value_04', 'factor': 1.04},
    tags=("orchestration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
