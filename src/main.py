import streamlit as st
import tempfile
import os
from vector_store import pdf_verctorization, rag_chain


st.set_page_config(
    page_title="PDF Chat Assistant",
    page_icon="📚",
    layout="wide"
)

if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'messages' not in st.session_state:
    st.session_state.messages = []


st.title("📚 PDF Chat Assistant")
st.markdown("""
Upload a PDF file and chat with its contents using AI. The assistant will answer your questions based on the document's content.
""")

with st.sidebar:
    st.header("Upload PDF")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        temp_files = []
        try:
            for uploaded_file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    temp_files.append(tmp_file.name)
            
            vectorstore = pdf_verctorization(temp_files)
            st.session_state.vectorstore = vectorstore
            st.success("PDFs processed successfully! You can now ask questions about the documents.")
        except Exception as e:
            st.error(f"Error processing PDFs: {str(e)}")
        finally:
            for temp_file in temp_files:
                try:
                    os.unlink(temp_file)
                except:
                    pass
    else:
        st.warning("Please upload PDF files first.")   


st.header("Chat with your PDF")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask a question about your PDF"):
    if st.session_state.vectorstore is None:
        st.warning("Please upload PDF files first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            try:
                with st.spinner("Thinking..."):
                    response = rag_chain(prompt, st.session_state.vectorstore)
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error getting response: {str(e)}")
                st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}"}) 
