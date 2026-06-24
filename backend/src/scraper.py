from bs4 import BeautifulSoup
import requests


def scrape_wiki_page(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get (url, headers = headers)
    response.raise_for_status()

    soup = BeautifulSoup (response.text, "html.parser")


    title_element = soup.find("h1")
    if title_element:
        title = title_element.get_text(strip = True)
    elif soup.title:
        title = soup.title.get_text(strip = True)
    else:
        title = "Untitled"


    paragraphs = soup.find_all("p")

    clean_paragraphs = []
    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            clean_paragraphs.append(text)

    content = "\n\n".join(clean_paragraphs)

    return {
        "title": title,
        "content": content,
        "url": url
    }

if __name__ == "__main__":
    test_url = "https://en.wikipedia.org/wiki/Grand_Theft_Auto:_Vice_City"
    print(f"Scraping: {test_url}...")

    try:
        result = scrape_wiki_page(test_url)

        with open("html_doc.txt", "w") as file:
            file.write(f"Title: {result["title"]}\n\n")
            file.write(f"URL: {result["url"]}\n\n")
            file.write(f"Content: {result["content"]}\n\n")

    except Exception as e:
        print(f"Error occurred: {e}")