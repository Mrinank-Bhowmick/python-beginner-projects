from openai import OpenAI

def correct_grammar(text, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with statements, and your task is to convert them to standard English."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    corrected_text = response.choices[0].message.content.strip()
    return corrected_text