import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def response(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0,
        max_tokens=1000,
    )
    data = response["choices"][0]["text"]
    return data


while True:
    query = input(">> ")
    if query == "bye":
        break
    print(response(query))
