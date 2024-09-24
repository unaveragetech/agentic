# tests/test_utils.py

import unittest
from utils.web_crawler import WebCrawler
from utils.scraper import Scraper

class TestUtils(unittest.TestCase):

    def test_web_crawler(self):
        wc = WebCrawler()
        html_content = wc.crawl("https://example.com")  # Replace with a test URL or mock response
        self.assertIsNotNone(html_content)  # Check if content is returned

    def test_scraper(self):
        scraper = Scraper()
        html_content = "<h1>Title</h1><h2>Subtitle</h2>"
        headings = scraper.scrape(html_content)
        self.assertEqual(headings, ["Title", "Subtitle"])  # Check if headings are extracted correctly

if __name__ == '__main__':
    unittest.main()
