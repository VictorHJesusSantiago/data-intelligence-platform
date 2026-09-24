"""Data Governance Control 30: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.30",
    family="data_governance",
    title='Data Governance Control 30',
    description='Classification, stewardship, policy and retention controls',
    operation="timestamp",
    configuration={'field': 'event_time', 'target': 'data_governance_value_30'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
