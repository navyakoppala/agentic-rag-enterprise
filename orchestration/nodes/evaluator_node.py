from orchestration.state.agent_state import AgentState

def evaluator_node(state: AgentState):

    response = state["final_response"]

    score = 0.95

    print("Evaluation completed")

    return {
        "evaluation_score": score
    }