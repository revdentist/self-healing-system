import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
import os
import os
print(">>> KEY LOADED BY APP:", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




client = OpenAI()

def analyze_logs(logs):
    """Take a list of logs and use AI to summarize the root cause."""
    if not logs:
        return "No logs to analyze."

    text = "\n".join(logs)

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an SRE who finds root causes."},
            {"role": "user", "content": f"Analyze these logs:\n{text}"}
        ]
    )

    return res.choices[0].message.content.strip()
