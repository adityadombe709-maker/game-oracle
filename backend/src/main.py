from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    bot_response = f"BotBackend: Your query: {user_query}"

    return {"botResponse": bot_response}
