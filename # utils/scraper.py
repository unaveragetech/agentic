# utils/scraper.py

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        pass

    def scrape(self, html_content):
        # Scrape the desired information from the HTML content
        print("Scraping data...")
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Extracting all headings (h1, h2, etc.)
        headings = [heading.text for heading in soup.find_all(['h1', 'h2', 'h3'])]
        return headings
