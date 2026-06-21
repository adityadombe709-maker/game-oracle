import chromadb
import uuid

client = chromadb.PersistentClient (path = "./chromadb_data")

collection = client.get_or_create_collection(name="gaming_wikis")
sample_docs = ["Minecraft is a block-building survival game.", "Elden Ring is a fantasy action RPG."]

def add_wiki_content(docs, meta):
    ids = []
    for _ in docs:
        ids.append(str(uuid.uuid4()))

    collection.add(ids=ids, documents=docs, metadatas=meta)


def search_gaming_knowledge(query):
    return collection.query(query_texts=[query], n_results = 1)


if __name__ == "__main__":

    sample_docs = ["Minecraft is a block-building survival game.", "Elden Ring is a fantasy action RPG."]

    sample_meta = [
        {"source": "test_minecraft"},
        {"source": "test_elden_ring"}
    ]

    print ("Adding sample content to chromaDB...")

    add_wiki_content (sample_docs, sample_meta)

    query_str = "RPG game"

    print(f"\nSearching for: '{query_str}'")
    results = search_gaming_knowledge (query_str)

    print ("\nResults: ")
    print (results)