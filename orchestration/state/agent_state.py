from typing import TypedDict, List

class AgentState(TypedDict):
    query: str

    retrieved_docs: List[str]

    tool_results: List[str]

    final_response: str

    evaluation_score: float