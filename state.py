from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    question: str
    safe: Optional[bool]
    intent: Optional[str]
    docs: Optional[List[dict]]
    answer: Optional[str]
    herbs: Optional[List[str]]