# PDF Reader

An AI-powered PDF question-answering tool. It loads a PDF with LangChain, splits and embeds the text into a Chroma vector store, summarises the document with an OpenAI model, and answers user questions about the content interactively.

## How to run

```
pip install -r requirements.txt
```

Set your OpenAI API key in a `.env` file as `API_KEY`, place the PDF in the folder, then:

```
python PDF_Reader.py
```

## Dependencies

- openai, langchain, chromadb, pypdf and others (see `requirements.txt`)

## Pyodide-runnable

No — it makes network calls to the OpenAI API and depends on LangChain/Chroma, none of which work in a browser sandbox.
