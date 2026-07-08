from ollama import chat
from pydantic import BaseModel


class Obj(BaseModel):
    status: str
    answer: str | None = None
    url: str | None = None


def generate_answer(query: str, context: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are GameOracle, a factual gaming search assistant.",
        },
        {
            "role": "user",
            "content": (
                f"Context:\n{context}\n\n"
                f"Question:\n{query}\n\n"
                f"Instructions: Answer the question using ONLY the context provided above. "
                f"If the context does not contain the answer, you MUST reply exactly with: "
                f"'I cannot find the answer in the provided search results.' Do not make up facts."
            ),
        },
    ]

    stream = chat(
        model="llama3.2:latest",
        messages=messages,
        stream=True,
        options={"temperature": 0.0},
    )

    full_response = ""
    for chunk in stream:
        text = chunk["message"]["content"]
        full_response += text

    return full_response


def generate_exploration_decision(
    query: str, page_content: str, links_list: str
) -> dict:
    messages = [
        {
            "role": "system",
            "content": "You are GameOracle, a factual gaming search assistant.",
        },
        {
            "role": "user",
            "content": (
                f"Page Content:\n{page_content}\n\n"
                f"Available Links:\n{links_list}\n\n"
                f"Question:\n{query}\n\n"
                f"Instructions: Answer the question using ONLY the context provided above. "
                f"If you have the answer, set the status as 'ANSWER' and the 'answer' field with your response. "
                f"Otherwise, set the status as 'EXPLORE' and the 'url' field with the target link."
            ),
        },
    ]

    output = chat(
        model="llama3.2:latest",
        messages=messages,
        options={"temperature": 0},
        format=Obj.model_json_schema(),
    )

    response = output["message"]["content"]
    return Obj.model_validate_json(response).model_dump()


if __name__ == "__main__":
    with open("backend/html_docs.txt", "r") as file:
        page_content = file.read()
    with open("backend/links.txt", "r") as file:
        links = file.read()

    answer = generate_exploration_decision(
        "who is the main protagonist of the game?", page_content, links
    )
    print(answer)
