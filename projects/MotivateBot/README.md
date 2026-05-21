# MotivateBot

Generates an inspirational message using the OpenAI GPT API. Given a prompt, it calls the OpenAI completion endpoint and prints the generated motivational text.

## How to run

```
pip install openai
```

Set your OpenAI API key in `main.py`, then:

```
python main.py
```

## Dependencies

- openai

## Pyodide-runnable

No — it makes network requests to the OpenAI API, which is not possible from a browser sandbox.
