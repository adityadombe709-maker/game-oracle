from ollama import chat


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
        options={"temperature": 0.6},
    )

    full_response = ""
    for chunk in stream:
        text = chunk["message"]["content"]
        full_response += text

    return full_response


if __name__ == "__main__":
    with open("backend/html_docs.txt", "r") as file:
        page_content = file.read()
    with open("backend/links.txt", "r") as file:
        links = file.read()

    answer = generate_exploration_decision(
        "who is the main protagonist of the game?", page_content, links
    )
    print(answer)
