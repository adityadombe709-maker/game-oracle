from data import add_wiki_content
from scraper import scrape_wiki_page

urls = [
    "https://en.wikipedia.org/wiki/Minecraft",
    "https://en.wikipedia.org/wiki/Elden_Ring",
    "https://en.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
    "https://en.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt"
]
contents = []
metas = []
for url in urls:
    try:
        contents.append(scrape_wiki_page(url)["content"])
        metas.append({"source": url})
    except Exception as e:
        print(f"Error occurred: {e}")

add_wiki_content (contents, metas)