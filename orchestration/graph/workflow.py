from langgraph.graph import StateGraph, END

from orchestration.state.agent_state import AgentState

from orchestration.nodes.retriever_node import retriever_node
from orchestration.nodes.generator_node import generator_node
from orchestration.nodes.evaluator_node import evaluator_node

workflow = StateGraph(AgentState)

# add nodes
workflow.add_node("retrieve", retriever_node)

workflow.add_node("generate", generator_node)

workflow.add_node("evaluate", evaluator_node)

# define flow
workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "generate")

workflow.add_edge("generate", "evaluate")

workflow.add_edge("evaluate", END)

graph = workflow.compile()