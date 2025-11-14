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

## 🚀 Getting Started

### **1. Clone the repo**

```bash
git clone https://github.com/subhashgowdak/Agentic-Chat-bot.git
cd Agentic-Chat-bot
```

### **2. Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.\\.venv\\Scripts\\activate       # Windows
```

### **3. Install dependencies**

```bash
pip install -r Requirements.txt
```

### **4. Make sure Ollama is running**

Install Ollama from [https://ollama.com](https://ollama.com)

Download models used in code (or change names):

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

### **5. Run the chatbot**

```bash
python main.py
```

Type your questions, type `q` to exit.

## 📦 Dataset

The repository includes a small file: **people-100.csv**

* Rows are converted into text documents
* Stored inside Chroma
* Retrieved based on similarity to your question

## 📝 Example Interaction

```
Enter your question: Who is John?

Retrieved context added...
Bot: "John is ..." (based on CSV data)
```

## 📜 License

This project is licensed under the **Apache 2.0 License**.
