import requests as _requests
import bs4 as _bs4
import constants as _constants

def _create_url(tag: str = "love") -> str:
    return f"https://www.goodreads.com/quotes/tag/{tag}"

def get_page(url: str) -> _bs4.BeautifulSoup:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = _requests.get(url, headers=headers)
    if page.status_code != 200:
        raise Exception(f"Failed to fetch page: {url}, Status Code: {page.status_code}")
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def _extract_quote_and_author(quote):
    quote_text=quote.contents[0].text.strip()
    author=quote.find(class_="authorOrTitle").text.strip()

    return quote_text, author
    
def scrape_quotes():
    collection=list()
    for tag in _constants.TAGS:
        url = _create_url(tag)
        soup = get_page(url)
        quotes = soup.find_all(class_="quoteText")
        for quote in quotes:
            quote_text, author = _extract_quote_and_author(quote)
            data=dict({"quote":quote_text, "author":author, "tag":tag})
            collection.append(data)
    return collection   
print(scrape_quotes())