import requests
import sys

from bs4 import BeautifulSoup

from scrapingtools import scrape_safely


@scrape_safely
def scrape_posted_date(soup):
    result = soup.select("html body div#main-content div.header p.left")
    return result[0].text if result else None


@scrape_safely
def scrape_teaser(soup):
    result = soup.select("html body div#main-content div.main-description")
    return result[0].text[:300] if result else None


def scrape_details(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla-Firefox"})
    soup = BeautifulSoup(response.text, 'html.parser')
    return {
        "posted_date": scrape_posted_date(soup),
        "teaser": scrape_teaser(soup),
    }


def main():
    print(scrape_details("http://www.cebujobs.ph/job/sr-python-developer-at-smart-source-inc"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
