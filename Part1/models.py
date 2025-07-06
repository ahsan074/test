from pydantic import BaseModel

class ToolResult(BaseModel):
    tool_used: str
    result: str

class EvaluationResult(BaseModel):
    test_name: str
    passed: bool
    reason: str
