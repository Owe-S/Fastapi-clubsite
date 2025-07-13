import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatgpt(prompt: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return resp.choices[0].message.content