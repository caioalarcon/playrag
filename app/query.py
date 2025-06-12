import os
from app.utils.s3 import download_index
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

LOCAL_INDEX = "faiss_store/local.index"
BUCKET = os.getenv('AWS_S3_BUCKET')
S3_KEY = os.getenv('AWS_S3_INDEX_KEY')

if not os.path.exists(LOCAL_INDEX):
    download_index(BUCKET, S3_KEY, LOCAL_INDEX)

embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.load_local(LOCAL_INDEX, embeddings)
retriever = vectorstore.as_retriever()
llm = OpenAI(temperature=0)
chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def answer_question(question: str):
    return chain.run(question)
