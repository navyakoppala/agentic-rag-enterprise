import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def generate_answer(
    question,
    context,
    history=""
):

    prompt = f"""
You are an Enterprise AI Document Assistant.

Your job is to answer ONLY using the provided document context.

Conversation History:
{history}

Retrieved Context:
{context}

User Question:
{question}

Rules:

Instructions:

1. Answer using document context.
2. If user asks analysis or interpretation,
   use retrieved values to infer.
3. Do not hallucinate.
4. If information is completely absent,
   say:
   "I could not find this information in the document."

Answer:
"""

    try:

        response = client.chat.completions.create(

            model=os.getenv(
                "MODEL_NAME",
                "llama-3.3-70b-versatile"
            ),

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.1,

            max_tokens=1024
        )

        answer = (
            response
            .choices[0]
            .message
            .content
        )

        return answer

    except Exception as e:

        return (
            f"Generation Error: {str(e)}"
        )