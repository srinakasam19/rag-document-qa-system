# RAG Document Question Answering System

## Overview

This project implements a **Retrieval-Augmented Generation (RAG) pipeline** that allows users to ask questions about documents. The system processes documents from a folder, converts them into embeddings, stores them in a vector database, and retrieves relevant information to generate accurate answers using a Large Language Model (LLM).

Instead of sending the entire document to the LLM, the system retrieves only the most relevant chunks, making the responses **more efficient, accurate, and context-aware**.

---

## Features

* Document ingestion from a folder path
* text chunking
* Embedding generation for document chunks
* Storage of embeddings in a vector database
* Semantic search using vector similarity
* Context retrieval for user queries
* Answer generation using an LLM
* Efficient Retrieval-Augmented Generation workflow

---

## Architecture

User Query
↓
Vector Search
↓
Retrieve Relevant Document Chunks
↓
Send Context + Query to LLM
↓
Generate Answer

---

## Project Workflow

1. **Document Loading**

   * Reads files from the specified folder path.

2. **Text Chunking**

   * Documents are split into smaller chunks for better retrieval.

3. **Embedding Generation**

   * Each chunk is converted into embeddings using an embedding model.

4. **Vector Storage**

   * Embeddings are stored in a vector database.

5. **Query Processing**

   * User query is converted into an embedding.

6. **Similarity Search**

   * The vector database retrieves the most relevant document chunks.

7. **Answer Generation**

   * Retrieved context is sent to an LLM to generate a final response.

---

## Technologies Used

* Python
* Embedding Models
* Vector Databases
* Large Language Models (LLMs)
* RAG (Retrieval-Augmented Generation)

---

## Example Use Case

Input Question:

```
What are the key points discussed in the document?
```

System Process:

* Retrieve relevant document chunks
* Send context to LLM
* Generate a summarized answer

Output:

```
The document discusses the main objectives, key findings, and conclusions related to the topic.
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/rag-document-qa-system.git
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Run the main script and provide the folder path containing documents.

Example:

```
python main.py
```

Enter your question and the system will return answers based on the document content.

---

## Future Improvements

* Add support for multiple document formats
* Implement streaming responses
* Add source citations for retrieved documents
* Build a web interface for interaction
* Improve retrieval ranking

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* LLM-based Question Answering
* Document Intelligence Systems

---

## Author

**Laxmi Srina**

BTech – Computer Science Engineering (AI & ML)

Interested in Artificial Intelligence, Machine Learning, and building intelligent systems.
