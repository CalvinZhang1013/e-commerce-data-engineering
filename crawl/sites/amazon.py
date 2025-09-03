# crawl/sites/amazon.py

from bs4 import BeautifulSoup

def parse(html: str) -> dict:
    """
    Parse Amazon product page HTML into a structured dict.
    This is a simplified demo — real Amazon HTML 可能会更复杂，还需定制。
    """

    soup = BeautifulSoup(html, "html.parser")

    data = {
        "product_id": soup.find("input", {"id": "ASIN"})["value"] if soup.find("input", {"id": "ASIN"}) else None,
        "title": soup.select_one("#productTitle").get_text(strip=True) if soup.select_one("#productTitle") else None,
        "price": soup.select_one(".a-price .a-offscreen").get_text(strip=True) if soup.select_one(".a-price .a-offscreen") else None,
        "currency": "USD",  # 简化处理，可以后续在 pipelines/normalize.py 里清洗
        "seller": soup.select_one("#sellerProfileTriggerId").get_text(strip=True) if soup.select_one("#sellerProfileTriggerId") else None,
        "rating": soup.select_one("span[data-asin] i span").get_text(strip=True) if soup.select_one("span[data-asin] i span") else None,
        "reviews_count": soup.select_one("#acrCustomerReviewText").get_text(strip=True) if soup.select_one("#acrCustomerReviewText") else None,
    }

    return data
