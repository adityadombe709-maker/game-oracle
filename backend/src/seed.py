from data import add_wiki_content
from scraper import scrape_wiki_page, scrape_fandom
from collections import deque
import time

url_witcher = "https://witcher.fandom.com/api.php?action=parse&format=json&page=The_Witcher_3:_Wild_Hunt"

q = deque()
links_added = []
chunks = []
links_popped = []


def url_seeder(url: str):
    scraper = scrape_fandom(url)
    curr_chunks = scraper["html"]
    curr_links = scraper["links"]

    chunks.extend(curr_chunks)
    with open("backend/witcher_chunks.txt", "a") as file:
        file.write("\n\n".join(curr_chunks) + "\n\n")

    for link in curr_links:
        if link not in links_added:
            q.append(link)
            links_added.append(link)

    links_popped.append(q.popleft())


def seed_game(url: str):
    q.append(url)
    links_added.append(url)
    max_urls = 500
    curr_urls = 0
    while q and curr_urls < max_urls:
        url_seeder(q[0])
        curr_urls = curr_urls + 1
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        seed_game(url_witcher)
        chunks_refined = "\n\n".join(chunks)
        with open("backend/witcher_chunks.txt", "w") as file:
            file.write(chunks_refined)
        print("\n".join(links_popped))

    except Exception as err:
        print(err)
