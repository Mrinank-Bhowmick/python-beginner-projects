from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)

with open("projects/Chat-GPT-Discord-Bot/GPT_Parameters.json") as f:
    data = json.load(f)

gpt_api_key = os.getenv("GPT_API_KEY")

char_limit = data["system_content"][0]["character_limit_prompt"]

def correct_grammar(prompt):
    client = OpenAI(api_key= gpt_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": data["system_content"][0]["correct_grammar"] + char_limit
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        # max_tokens=64,
        top_p=1
    )
    output = response.choices[0].message.content.strip()
    return output

def single_page_website(prompt):
    client = OpenAI(api_key= gpt_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": data["system_content"][0]["single_page_website"] + char_limit
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        # max_tokens=1050,
        top_p=1
    )
    output = response.choices[0].message.content.strip()
    return output

def text_to_emoji(prompt):
    client = OpenAI(api_key= gpt_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": data["system_content"][0]["text_to_emoji"] + char_limit
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1.2,
        # max_tokens=800,
        top_p=1
    )
    output = response.choices[0].message.content.strip()
    return output

def text_to_block_letters(prompt):
    client = OpenAI(api_key= gpt_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": data["system_content"][0]["text_to_block_letters"] + char_limit
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        # max_tokens=800,
        top_p=1
    )
    output = response.choices[0].message.content.strip()
    return output