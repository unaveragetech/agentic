# utils/web_crawler.py

import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url):
        # Crawl a given URL and return the HTML content
        if url in self.visited_urls:
            print(f"Already visited {url}. Skipping...")
            return None
        
        print(f"Crawling URL: {url}")
        response = requests.get(url)
        
        if response.status_code == 200:
            self.visited_urls.add(url)
            return response.text
        else:
            print(f"Failed to crawl {url}. Status code: {response.status_code}")
            return None
