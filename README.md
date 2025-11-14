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

## 🙌 Author
