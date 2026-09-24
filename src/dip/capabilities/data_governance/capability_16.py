"""Data Governance Control 16: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.16",
    family="data_governance",
    title='Data Governance Control 16',
    description='Classification, stewardship, policy and retention controls',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_governance_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
