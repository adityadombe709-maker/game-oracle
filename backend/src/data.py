import os
import pickle

os.environ["ANONYMIZED_TELEMETRY"] = "False"

import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./chromadb_data",
)

# collection = client.get_or_create_collection(name="gaming_wikis")
# sample_docs = [
#     "Minecraft is a block-building survival game.",
#     "Elden Ring is a fantasy action RPG.",
# ]


def add_wiki_content(name, chunks, parent_url):
    size = len(chunks)
    metadatas = [{"source": parent_url}] * size
    collection = client.get_or_create_collection(name=name)
    ids = []
    for id in range(0, size):
        ids.append(str(uuid.uuid4()))
    collection.add(ids=ids, metadatas=metadatas, documents=chunks)


def search_gaming_knowledge(query, collection_name):
    collection = client.get_collection(name=collection_name)
    return collection.query(query_texts=[query], n_results=50)


def print_collection():
    all_data = collection.get()
    with open("backend/temp_texts/collection_docs.txt", "w") as file:
        file.write(str(all_data["metadatas"]))


def delete_collection():
    client.delete_collection(name="gaming_wikis")


if __name__ == "__main__":
    # with open("temp_texts/witcher_chunks_pickled.txt", "rb") as file:
    #     chunks = pickle.load(file)
    # name = "witcher3"
    # parent_url = "witcher.fandom.com"
    # add_wiki_content("witcher3", chunks, "witcher.fandom.com")
    query = "what is tor'haerne?"
    ans = search_gaming_knowledge(query, "witcher3")["documents"]
    print(ans)
