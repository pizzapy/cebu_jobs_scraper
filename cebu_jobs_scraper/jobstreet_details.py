import logging
import sys

import requests
from bs4 import BeautifulSoup

from .scrapingtools import scrape_safely


@scrape_safely
def scrape_company_industry(soup):
    result = soup.select("#company_industry")
    return result[0].text if result else None


@scrape_safely
def scrape_company_size(soup):
    result = soup.select("#company_size")
    return result[0].text if result else None


@scrape_safely
def scrape_working_hours(soup):
    result = soup.select("#work_environment_working_hours")
    return result[0].text if result else None


def scrape_details(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla-Firefox"})
    soup = BeautifulSoup(response.text, 'html.parser')
    return {
        "company_industry": scrape_company_industry(soup),
        "company_size": scrape_company_size(soup),
        "working_hours": scrape_working_hours(soup),
    }


def main():
    logging.basicConfig()
    print(scrape_details("http://www.jobstreet.com.ph/en/job/business-continuity-management-specialist-cebu-6601200?fr=J&src=5"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
