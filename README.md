# Agentic Chat Bot

A simple Python-based **retrieval‑augmented chatbot** built using **Ollama embeddings**, **Chroma vector store**, and a minimal terminal interface.

This repository demonstrates how to:

* Load and embed a dataset (CSV)
* Build a Chroma vector store
* Retrieve relevant documents for a user query
* Generate responses using an LLM from the Ollama ecosystem

This is a lightweight prototype suitable for learning, experimentation, and extending into your own agentic systems.

## 📁 Project Structure

```
Agentic-Chat-bot/
│
├── main.py              # Chat loop + LLM pipeline
├── vector.py            # Embeddings + Chroma vector store builder
├── people-100.csv       # Sample dataset used for retrieval
├── Requirements.txt     # Required dependencies
├── LICENSE
└── README.md
```

## ⚙️ How It Works

### 1. **Vector Store Creation** (`vector.py`)

* Loads `people-100.csv`
* Converts each row into a text document
* Embeds documents using **OllamaEmbeddings**
* Saves them in a local **Chroma** database

### 2. **Chatbot Flow** (`main.py`)

* Takes user question from terminal
* Retrieves the most relevant entries from vector DB
* Feeds both question + context to an Ollama LLM (example: `llama3.2`)
* Returns the generated answer
