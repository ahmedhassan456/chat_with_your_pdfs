# PDF Chat Assistant

A Streamlit-based RAG (Retrieval-Augmented Generation) application that allows users to upload PDF documents and chat with their content using AI.

## Features

- 📄 Upload multiple PDF documents
- 💬 Chat with the content of your PDFs
- 🔍 Semantic search across multiple documents
- 🚀 Powered by Groq's LLM and Ollama embeddings

## Prerequisites

- Python 3.8 or higher
- Ollama running locally (for embeddings)
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

4. Start Ollama (for embeddings):
```bash
ollama serve
```

## Project Structure

```
.
├── src/
│   ├── llm.py           # LLM configuration and chat functions
│   ├── rag_app.py       # RAG implementation and PDF processing
│   └── streamlit_app.py # Streamlit web interface
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run src/main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload PDFs:
   - Click the "Choose PDF files" button in the sidebar
   - Select one or more PDF files
   - Wait for the processing to complete

4. Chat with your PDFs:
   - Type your question in the chat input
   - The AI will respond based on the content of your uploaded PDFs

5. Manage PDFs:
   - View all uploaded PDFs in the sidebar
   - The vector store will automatically update when PDFs are added them

## Dependencies

- streamlit: Web application framework
- langchain: Framework for building LLM applications
- langchain-community: Community-maintained LangChain components
- langchain-groq: Groq LLM integration
- langchain-ollama: Ollama embeddings integration
- pymupdf: PDF processing library
- chromadb: Vector database for document storage
- python-dotenv: Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Groq for providing the LLM API
- Ollama for the embeddings model
- Streamlit for the web framework
- LangChain for the RAG framework
