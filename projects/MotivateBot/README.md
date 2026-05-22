# MotivateBot

Generates an inspirational message using the OpenAI GPT API. Given a prompt, it calls the OpenAI completion endpoint and prints the generated motivational text.

## Example

The script uses the fixed prompt `"You are capable of achieving great things because"` and prints the GPT-generated continuation, for example:

```text
you have the resilience to face challenges head-on and the creativity to find
solutions where others see only obstacles.
```

## How to run on localhost

```
pip install openai
```

Set your OpenAI API key in `main.py`, then:

```
python main.py
```

## Dependencies

- openai
