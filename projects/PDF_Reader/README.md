# PDF Reader

An AI-powered PDF question-answering tool. It loads a PDF with LangChain, splits and embeds the text into a Chroma vector store, summarises the document with an OpenAI model, and answers user questions about the content interactively.

## Example

```text
Text in pdf  ... [full extracted text from promptEngineering.pdf] ...
Summary of text in pdf  Prompt engineering is the practice of designing and
refining input prompts to guide large language models toward desired outputs...

INSTRUCTIONS:
Enter the question you want to ask from pdf text OR press "-1" to STOP
Enter your question: What is prompt engineering?
Prompt engineering is the process of crafting inputs that steer an AI model
to produce accurate, relevant, and useful responses.
Enter your question: -1
```

## How to run on localhost

```
pip install -r requirements.txt
```

Set your OpenAI API key in a `.env` file as `API_KEY`, place the PDF in the folder, then:

```
python PDF_Reader.py
```

## Dependencies

- openai, langchain, chromadb, pypdf and others (see `requirements.txt`)
