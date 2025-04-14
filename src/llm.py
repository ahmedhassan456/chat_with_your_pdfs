from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import logging
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))

def groq_llm(question, context):
    system_msg = SystemMessage(content=f"You are a helpful assistant answer only based on the context: {context}")
    human_msg = HumanMessage(content=question)
    response = llm.invoke([system_msg, human_msg])
    return response.content.strip()


