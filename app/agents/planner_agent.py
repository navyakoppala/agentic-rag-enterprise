def planner_agent(question):

    q = question.lower()

    if "summary" in q:
        return "summary"

    elif "compare" in q:
        return "analysis"

    elif "report" in q:
        return "report"

    else:
        return "retrieval"