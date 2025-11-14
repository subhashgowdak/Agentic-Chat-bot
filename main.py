from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from vector import retreiver

model=OllamaLLM(model="llama3.2")

template = """
You are a helpful assistant that helps people find information.
here are some relevant data: {data}
Please answer the following question: {question}
If you don't know the answer, just say that you don't know, don't try to make up an answer."""
prompt = ChatPromptTemplate.from_template(template)
chain=prompt | model

while True:
    print("\n\n--------------------------------------------------")
    question = input("Enter your question (or q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    data = retreiver.invoke(question)
    response=chain.invoke({"data":data,"question":question})
    print(response)