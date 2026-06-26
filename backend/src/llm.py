from ollama import chat

def generate_answer(query: str, context: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are GameOracle, a factual gaming search assistant."
        },
        {
            "role": "user", 
            "content": (
                f"Context:\n{context}\n\n"
                f"Question:\n{query}\n\n"
                f"Instructions: Answer the question using ONLY the context provided above. "
                f"If the context does not contain the answer, you MUST reply exactly with: "
                f"'I cannot find the answer in the provided search results.' Do not make up facts."
            )
        }
    ]

    stream = chat(model = "llama3.2:latest", messages = messages, stream = True, options = {"temperature": 0.0})

    full_response = ""
    for chunk in stream:
        text = chunk["message"]["content"]
        full_response += text

    return full_response

if __name__ == "__main__":
    test_query = "who is the antagonist of the game gta vice city?"
    test_context = "Grand Theft Auto: Vice City follows gangster Tommy Vercetti's rise to power after being released from prison."

    print("Generating answer from ollama...")
    answer = generate_answer(test_query, test_context)

    print("\n--- Generated Answer ---")
    print(answer)
    print("----------------")
