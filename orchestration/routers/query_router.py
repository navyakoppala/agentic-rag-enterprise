def route_query(query: str):

    if "code" in query:
        return "coding"

    elif "research" in query:
        return "retrieval"

    return "general"