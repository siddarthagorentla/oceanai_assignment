from pydantic import BaseModel
from typing import List, Optional

class TestCase(BaseModel):
    Test_ID: str
    Feature: str
    Test_Scenario: str
    Expected_Result: str
    Grounded_In: str

class TestCaseResponse(BaseModel):
    test_cases: List[TestCase]

class ScriptRequest(BaseModel):
    test_case: TestCase
    html_content: Optional[str] = None

class ScriptResponse(BaseModel):
    script_code: str
    explanation: str
