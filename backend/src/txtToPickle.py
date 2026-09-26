import pickle

with open("backend/temp_texts/sekiro_chunks.txt", "r") as file:
    chunks = file.read()

with open("backend/temp_texts/sekiro_chunks_pickled.txt", "wb") as file:
    pickle.dump(chunks, file)
