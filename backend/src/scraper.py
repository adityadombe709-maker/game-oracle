from bs4 import BeautifulSoup, SoupStrainer
import requests
import html2text
from data import add_wiki_content
from urllib.parse import urlsplit
from make_chunks import make_chunks


# helper function to choose urls
def link_selector(link: str) -> bool:
    if link.startswith("/wiki") and all(
        ext not in link for ext in ("png", "jpg", "jpeg")
    ):
        return True
    return False


# scrape wikipedia
def scrape_wiki_page(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title_element = soup.find("h1")
    if title_element:
        title = title_element.get_text(strip=True)
    elif soup.title:
        title = soup.title.get_text(strip=True)
    else:
        title = "Untitled"

    paragraphs = soup.find_all("p")

    clean_paragraphs = []
    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            clean_paragraphs.append(text)

    content = "\n\n".join(clean_paragraphs)

    return {"title": title, "content": content, "url": url, "response": response}


# give api path from page name
def resolve_wiki_link(parent_url: str, relative_url: str) -> str:
    split_url = urlsplit(parent_url)
    relative_url = relative_url.replace("/wiki/", "")
    query = "?action=parse&format=json&page="
    new_url = (
        f"{split_url.scheme}://{split_url.netloc}{split_url.path}{query}{relative_url}"
    )

    return new_url


def scrape_fandom(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(url, headers=headers)
    html = response.json()["parse"]["text"]["*"]

    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.body_width = 0

    soup = BeautifulSoup(html, "html.parser", parse_only=SoupStrainer("a"))
    anchors = []
    links = []
    for link in soup:
        if link.has_attr("href"):
            if link_selector(link["href"]):
                links.append(link["href"])
                anchors.append(link.text)

    html_refined = h.handle(html)
    links = [resolve_wiki_link(url, link) for link in links]
    links_refined = str("\n".join(links))

    html_chunks = make_chunks(html_refined)
    return {"html": html_chunks, "links": links}


if __name__ == "__main__":
    test_url = "https://witcher.fandom.com/api.php?action=parse&format=json&page=The_Witcher_3:_Wild_Hunt"
    test_url2 = "https://gta.fandom.com/api.php?action=parse&format=json&page=Grand_Theft_Auto:_Vice_City"
