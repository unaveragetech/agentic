# utils/web_crawler.py

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, user_agent="Mozilla/5.0", timeout=10):
        """
        Initialize the WebCrawler with user agent and timeout settings.
        
        Args:
            user_agent (str): The user agent string for HTTP requests.
            timeout (int): Timeout duration for requests in seconds.
        """
        self.visited_urls = set()
        self.user_agent = user_agent
        self.timeout = timeout

    def crawl(self, url):
        """
        Crawl a given URL and return the page content.
        
        Args:
            url (str): The URL to crawl.

        Returns:
            str: The HTML content of the page, or None if the request failed.
        """
        if url in self.visited_urls:
            print(f"Already visited {url}. Skipping...")
            return None

        headers = {'User-Agent': self.user_agent}
        print(f"Crawling URL: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()  # Raise an error for bad responses
            self.visited_urls.add(url)  # Track visited URLs
            return response.text
        except RequestException as e:
            print(f"Error crawling {url}: {e}")
            return None

    def extract_links(self, html_content):
        """
        Extract all hyperlinks from the provided HTML content.
        
        Args:
            html_content (str): The HTML content from which to extract links.

        Returns:
            list: A list of extracted URLs.
        """
        if not html_content:
            return []
        
        soup = BeautifulSoup(html_content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

    def crawl_and_extract(self, url):
        """
        Crawl a URL and extract hyperlinks from the page.
        
        Args:
            url (str): The URL to crawl.

        Returns:
            tuple: The HTML content and a list of extracted URLs.
        """
        html_content = self.crawl(url)
        links = self.extract_links(html_content)
        return html_content, links

    def clear_visited_urls(self):
        """Clear the set of visited URLs."""
        self.visited_urls.clear()
        print("Cleared visited URLs.")

