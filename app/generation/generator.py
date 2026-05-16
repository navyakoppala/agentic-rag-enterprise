import os

import google.generativeai as genai

from dotenv import load_dotenv

# LOAD ENV
load_dotenv()

# CONFIGURE GEMINI
genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

# CREATE MODEL
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)

# GENERATE ANSWER
def generate_answer(
    question,
    context
):

    prompt = f"""
You are an intelligent enterprise AI assistant.

Answer ONLY from the provided context.

If answer is not found in context,
say:
'I could not find this information in the document.'

Context:
{context}

Question:
{question}

Provide concise professional answers.
"""

    response = model.generate_content(
        prompt
    )

    return response.text