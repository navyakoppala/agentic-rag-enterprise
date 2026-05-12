# Agentic RAG Enterprise Project

This is an agentic Retrieval-Augmented Generation (RAG) system for enterprise use, specifically designed for querying HR policies or similar documents.

## Features

- PDF document ingestion and text extraction
- Text chunking with overlap
- Vector embeddings using Sentence Transformers
- Vector storage with ChromaDB
- Retrieval of relevant context
- Answer generation using Google's Gemini AI

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Gemini API key:
   - Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Add it to the `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. Place your PDF document in the `data/` folder (e.g., `hr_policy.pdf`)

## Usage

Run the main script:
```
python main.py
```

This will:
- Load and index the PDF document
- Start an interactive chat interface

Ask questions about the document, and the system will provide answers based on the content.

Type "exit" to quit the chat.

## Project Structure

- `main.py`: Entry point, sets up RAG and starts chat
- `app/ingestion/loader.py`: PDF loading and text extraction
- `app/retrieval/embedder.py`: Text chunking and embedding creation
- `app/retrieval/vectordb.py`: Vector database operations
- `app/retrieval/retriever.py`: Context retrieval
- `app/generation/generator.py`: Answer generation with Gemini
- `app/agents/rag_agent.py`: Main RAG logic
- `data/`: Folder for documents
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (API keys)