# /api/index.py

from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import AIMessage,HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.chains import create_history_aware_retriever,create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from pydantic import  BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}