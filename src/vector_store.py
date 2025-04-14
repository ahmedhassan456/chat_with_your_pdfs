from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from llm import groq_llm
import logging
from langchain_ollama import OllamaEmbeddings
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tokenizer = OllamaEmbeddings(model="all-minilm:33m-l12-v2-fp16", base_url="http://localhost:11434")

def pdf_verctorization(pdf_paths: List[str]):
    all_docs = []
    for pdf_path in pdf_paths:
        try:
            loader = PyMuPDFLoader(pdf_path)    
            docs = loader.load()
            if docs:
                all_docs.extend(docs)
            else:
                logging.warning(f"No content found in PDF: {pdf_path}")
        except Exception as e:
            logging.error(f"Error loading PDF {pdf_path}: {str(e)}")
            continue
    
    if not all_docs:
        raise ValueError("No valid content found in any of the PDFs")
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=10)
    spletted_docs = splitter.split_documents(all_docs)
    
    if not spletted_docs:
        raise ValueError("No valid chunks created from the PDFs")
    
    
    vectorstore = Chroma.from_documents(spletted_docs, embedding=tokenizer)
    return vectorstore


def rag_chain(question, vectorstore):
    if vectorstore is None:
        raise ValueError("No PDF has been processed yet. Please upload a PDF first.")
    retriever = vectorstore.as_retriever()
    docs = retriever.invoke(question)
    logging.info(f"Docs:\n {docs}")
    context = "\n\n".join([doc.page_content for doc in docs])
    return groq_llm(question, context)