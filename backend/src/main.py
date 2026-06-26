from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.data import search_gaming_knowledge
from src.llm import generate_answer

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Backend is running"}


class QueryRequest(BaseModel):
    query: str


@app.post("/api/search")
def search(request: QueryRequest):
    user_query = request.query
    results = search_gaming_knowledge(user_query)
    if results and results["documents"] and results["documents"][0]:
        first_match = results["documents"][0][0]
    else:
        first_match = "No results found"

    answer = generate_answer(user_query, first_match)
    bot_response = f"BotBackend: {answer}"

    return {"botResponse": bot_response}
