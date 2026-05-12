import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_answer(question, context):

    combined_context = "\n".join(context)

    prompt = f"""
You are an enterprise AI assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
say:
"I could not find this information in the enterprise documents."

Context:
{combined_context}

Question:
{question}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"API Error: {str(e)}"