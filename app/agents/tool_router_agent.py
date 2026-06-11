def route_tool(question):

    q = question.lower()

    if "my name" in q:
        return "memory"

    if "document" in q:
        return "rag"

    if "latest" in q:
        return "web"

    return "rag"