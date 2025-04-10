import requests
from bs4 import BeautifulSoup

HEADERS = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = url
        self.title, self.text = self._scrape(self.url)

    def _scrape(self, url: str):
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        
        for tag in soup(["script", "style", "img", "input", "nav", "footer", "aside"]):
            tag.decompose()

        text = soup.body.get_text(separator="\n", strip=True)
        return title, text
