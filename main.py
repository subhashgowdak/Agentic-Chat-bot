from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate

model=OllamaLLM(model="llama3.2")

template = """
You are a helpful assistant that helps people find information.
here are some relevant data: {data}
Please answer the following question: {question}
If you don't know the answer, just say that you don't know, don't try to make up an answer."""