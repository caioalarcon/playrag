from fastapi import FastAPI, Query
from app.query import answer_question

app = FastAPI()

@app.get("/ask")
def ask(question: str = Query(..., description="Question for RAG")):
    result = answer_question(question)
    return {"answer": result}
