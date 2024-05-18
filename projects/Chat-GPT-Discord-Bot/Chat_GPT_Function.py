from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)

with open("projects/Chat-GPT-Discord-Bot/GPT_Parameters.json") as f:
    data = json.load(f)

gpt_api_key = os.getenv("GPT_API_KEY")

correct_grammar_system_content = data["system_content"][0]["correct_grammar"]

def correct_grammar(prompt):
    client = OpenAI(api_key= gpt_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": correct_grammar_system_content
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    corrected_text = response.choices[0].message.content.strip()
    return corrected_text