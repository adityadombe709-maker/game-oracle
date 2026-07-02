from bs4 import BeautifulSoup
import requests
import html2text


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

    html_refined = h.handle(html)
    return html_refined


if __name__ == "__main__":
    test_url = "https://witcher.fandom.com/api.php?action=parse&format=json&page=The_Witcher_3:_Wild_Hunt"
    test_url2 = "https://gta.fandom.com/api.php?action=parse&format=json&page=Grand_Theft_Auto:_Vice_City"

    try:
        html = scrape_fandom(test_url)
        with open("backend/html_docs.txt", "w") as file:
            file.write(html)
    except Exception as e:
        print(f"Error occurred: {e}")
