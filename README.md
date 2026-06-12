# Agentic RAG Enterprise
An enterprise-grade Agentic Retrieval-Augmented Generation (RAG) platform for querying organizational documents such as HR policies, employee handbooks, compliance manuals, and internal knowledge bases.
## Features

* User Authentication (Login / Registration)
* PDF Upload and Processing
* Automatic Text Chunking
* Embedding Generation using Sentence Transformers
* Vector Storage using Qdrant
* Semantic Search and Retrieval
* Gemini-powered Answer Generation
* Chat Memory Support
* Multi-document Management
* Streamlit Web Interface

## Tech Stack

* Python
* Streamlit
* Google Gemini
* Qdrant Vector Database
* Sentence Transformers
* PyPDF
* RAG Architecture

## Installation

### Create Virtual Environment
```bash
python -m venv .venv
```
### Activate Environment

```bash
.venv\Scripts\activate
```
### Install Dependencies

```bash
pip install -r requirements.txt
```
### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```
## Run Application

```bash
streamlit run streamlit_app.py
```
## Project Structure

```text
app/
├── auth/
├── ingestion/
├── retrieval/
├── generation/
├── memory/
├── voice/
├── database/

streamlit_app.py
requirements.txt
README.md
```
## Usage

1. Register a new account
2. Login
3. Upload a PDF document
4. Wait for indexing to complete
5. Ask questions about the document
6. View AI-generated answers with retrieved context

## Future Enhancements

* Voice Assistant
* Multi-user Database
* Document Summarization
* Agent Routing
* Hybrid Search
* Role-based Access Control
