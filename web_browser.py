import requests
from typing import Optional

class WebBrowser:
    def __init__(self):
        self.session = requests.Session()

    def browse(self, url: str) -> Optional[str]:
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error browsing {url}: {e}")
            return None
