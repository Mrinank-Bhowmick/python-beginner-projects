from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai

# Set your OpenAI API key using the environment variable OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def chatgpt():
    # Get the incoming SMS message
    inb_msg = request.form["Body"].lower()

    # Print the incoming message for debugging
    print(inb_msg)

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        model="gpt-3.5-turbo", prompt=inb_msg, max_tokens=3000, temperature=0.7
    )

    # Create a response using Twilio's MessagingResponse
    resp = MessagingResponse()
    resp.message(response["choices"][0]["text"])

    return str(resp)


if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
