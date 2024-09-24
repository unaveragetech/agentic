# agents/low_level_agent.py

from utils.web_crawler import WebCrawler
from utils.scraper import Scraper
from utils.logger import Logger

class LowLevelAgent:
    def __init__(self, subtopic, retries=3, timeout=10):
        self.subtopic = subtopic
        self.crawler = WebCrawler(user_agent="Mozilla/5.0", timeout=timeout)
        self.scraper = Scraper()
        self.logger = Logger()
        self.retries = retries

    def conduct_research(self):
        url = f"https://example.com/search?q={self.subtopic}"  # Mock search URL
        for attempt in range(self.retries):
            self.logger.log_info(f"Crawling URL: {url} (Attempt {attempt + 1})")
            html_content = self.crawler.crawl(url)
            if html_content:
                return self.scraper.scrape(html_content)
            else:
                self.logger.log_error(f"Failed to retrieve data from {url}.")
        return None
