import requests
import sys

from bs4 import BeautifulSoup


def scrape_posted_date(soup):
    return soup.select("html body div#main-content div.header p.left")[0].text


def scrape_teaser(soup):
    return soup.select("html body div#main-content div.main-description")[0].text[:300]


def scrape_details(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla-Firefox"})
    soup = BeautifulSoup(response.text)
    return {
        "posted_date": scrape_posted_date(soup),
        "teaser": scrape_teaser(soup),
    }


def main():
    print(scrape_details("http://www.cebujobs.ph/job/sr-python-developer-at-smart-source-inc"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
