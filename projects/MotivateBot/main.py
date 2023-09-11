import openai

# Set up your OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key


def generate_inspirational_message(prompt):
    """Generate an inspirational message using GPT-3.5."""
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    prompt = "You are capable of achieving great things because"
    message = generate_inspirational_message(prompt)
    print(message)
