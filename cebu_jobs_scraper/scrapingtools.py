import logging

logger = logging.getLogger("cebu_jobs_scraper")


def scrape_safely(func):
    def scrape_safely_decorator(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result.strip() if isinstance(result, str) else None
        except Exception as e:
            logger.warn("Could not scrape safely with {}: {}".format(func.__name__, e))
            return None

    return scrape_safely_decorator
