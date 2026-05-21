from orchestration.state.agent_state import AgentState

def retriever_node(state: AgentState):

    query = state["query"]

    # simulate retrieval
    docs = [
        "Document 1",
        "Document 2"
    ]

    print("Retrieved docs")

    return {
        "retrieved_docs": docs
    }