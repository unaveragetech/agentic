# utils/web_crawler.py

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, user_agent, timeout):
        self.visited_urls = set()
        self.user_agent = user_agent
        self.timeout = timeout

    def crawl(self, url):
        if url in self.visited_urls:
            print(f"Already visited {url}. Skipping...")
            return None

        headers = {'User-Agent': self.user_agent}
        print(f"Crawling URL: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            self.visited_urls.add(url)
            return response.text
        except RequestException as e:
            print(f"Error crawling {url}: {e}")
            return None

