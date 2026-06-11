class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add_message(
        self,
        role,
        content
    ):
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_history(self):

        history = ""

        for msg in self.messages:

            history += (
                f"{msg['role']}: "
                f"{msg['content']}\n"
            )

        return history

    def clear(self):
        self.messages = []