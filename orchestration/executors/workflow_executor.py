from orchestration.graph.workflow import graph

def execute_workflow(query: str):

    result = graph.invoke({
        "query": query
    })

    return result