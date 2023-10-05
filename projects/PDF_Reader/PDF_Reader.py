import os
import re
import openai
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
openai_api_key = os.getenv("API_KEY")
openai.openai_api_key = openai_api_key

loader = PyPDFLoader("promptEngineering.pdf")
docs = loader.load_and_split()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


def originalText(docs):
    text = str(docs)
    regex = r"(Document)|(page_content=)|(metadata={'source':)|('page': \d})\)|(\\n)"
    text = re.sub(regex, "", text)
    return text


text = originalText(docs)
print("Text in pdf", text)


def summarizeText():
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    chain = load_summarize_chain(llm, chain_type="stuff")
    return chain.run(docs)


summary = summarizeText()
print("Summary of text in pdf", summary)


def QA(query):
    qa = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0), vectorstore.as_retriever(), memory=memory
    )
    query = "What is prompt engineering?"
    result = qa({"question": query})
    result = str(result["chat_history"][1])
    result = result.split("content='")[1]
    return result


print("INSTRUCTIONS:")
print('Enter the question you want to ask from pdf text OR press "-1" to STOP')
while True:
    user_input = input("Enter your question: ")
    if user_input == "-1":
        break
    else:
        print(QA(user_input))
