# agents/low_level_agent.py

from utils.web_crawler import WebCrawler
from utils.scraper import Scraper

class LowLevelAgent:
    def __init__(self, subtopic):
        self.subtopic = subtopic
        self.crawler = WebCrawler(user_agent="Mozilla/5.0", timeout=10)
        self.scraper = Scraper()

    def conduct_research(self):
        url = f"https://example.com/search?q={self.subtopic}"  # Mock search URL
        html_content = self.crawler.crawl(url)
        if html_content:
            return self.scraper.scrape(html_content)
        return None
