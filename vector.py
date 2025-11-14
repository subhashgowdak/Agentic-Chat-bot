from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("people-100.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content= row["First Name"] + row["Sex"] + row["Email"] + row["Phone"] + row["Job Title"],
            metadata= {"id": row["User Id"], "dob": row["Date of birth"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vectorstore = Chroma(
    collection_name="people",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vectorstore.add_documents(documents, ids=ids)
    
retreiver = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)