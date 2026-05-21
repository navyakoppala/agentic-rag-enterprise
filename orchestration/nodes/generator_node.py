from orchestration.state.agent_state import AgentState

def generator_node(state: AgentState):

    docs = state["retrieved_docs"]

    response = f"Generated answer using {docs}"

    return {
        "final_response": response
    }