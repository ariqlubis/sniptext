from openai import OpenAI
from sniptext.website import Website
from sniptext.config import MODEL

client = OpenAI(base_url="http://localhost:11434/v1", api_key="gemma")

SYSTEM_PROMPT = (
    "You are an assistant like Bloomberg AI (but in general) that analyzes a website's content "
    "and summarizes it in clean, terminal-friendly plain text.\n"
    "Use simple indentation, bullet points (- or *), and clear section headers in uppercase.\n"
    "Avoid using Markdown formatting"
    "Avoid using asterik '*'."
)

def build_prompt(website: Website):
    user_prompt = f"Website Title: {website.title}\n\n"
    user_prompt += (
        "Here is the content of the website. Please summarize it concisely. "
        "If it's news, include the headline and a short summary.\n\n"
    )

    user_prompt += website.text
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

def summarize(url: str) -> str:
    website = Website(url)
    response = client.chat.completions.create(
        model=MODEL,
        messages=build_prompt(website),
        stream=True
    )

    summary = ""
    for chunk in response:
        delta = chunk.choices[0].delta
        if hasattr(delta, 'content') and delta.content:
            print(delta.content, end='', flush=True)  # live output in terminal
            summary += delta.content  # collect full text
