"""Data Governance Control 03: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.03",
    family="data_governance",
    title='Data Governance Control 03',
    description='Classification, stewardship, policy and retention controls',
    operation="project",
    configuration={'field': 'status', 'target': 'data_governance_value_03', 'fields': ['id', 'status', 'value']},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
