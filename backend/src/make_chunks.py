from langchain_text_splitters import RecursiveCharacterTextSplitter


def make_chunks(page_content: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, separators=["\n\n", "\n"], chunk_overlap=150
    )
    chunks = splitter.split_text(page_content)
    return chunks


if __name__ == "__main__":
    with open("backend/html_docs.txt", "r") as file:
        page_content = file.read()
    result = make_chunks(page_content)
    result_refined = (
        "\n<------------------------------------------------------->\n ".join(result)
    )
    with open("backend/chunks.txt", "w") as file:
        file.write(result_refined)
