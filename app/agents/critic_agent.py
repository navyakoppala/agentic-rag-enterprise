def critic_agent(
    answer,
    context
):

    if answer.lower().startswith(
        "i could not find"
    ):
        return answer

    if len(answer) < 20:
        return (
            answer +
            "\n\n[Low Confidence]"
        )

    return answer