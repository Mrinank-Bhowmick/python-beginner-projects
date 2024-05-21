from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

gpt_api_key = os.getenv("GPT_API_KEY")

def gpt(prompt: str, sys_prompt: str, temp: float):
    client = OpenAI(api_key= gpt_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temp,
        # max_tokens=64,
        top_p=1
    )
    output = response.choices[0].message.content.strip()
    return output