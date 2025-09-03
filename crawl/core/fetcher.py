# crawl/core/fetcher.py

import requests

def fetch(url: str, headers: dict = None) -> str:
    """
    Fetch HTML content from a URL.
    """
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36"
    }
    if headers:
        default_headers.update(headers)

    response = requests.get(url, headers=default_headers, timeout=15)
    response.raise_for_status()
    return response.text
