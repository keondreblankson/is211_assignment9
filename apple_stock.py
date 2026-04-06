# apple_stock.py
# Scrapes Apple historical stock data from Yahoo Finance
# URL: https://finance.yahoo.com/quote/AAPL/history?p=AAPL

import requests
from bs4 import BeautifulSoup


URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"


def main():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    if not table:
        print("Could not find the historical data table.")
        return

    rows = table.find_all("tr")

    for row in rows[1:]:
        cols = row.find_all("td")

        # Valid stock rows usually have 7 columns:
        # Date, Open, High, Low, Close*, Adj Close**, Volume
        if len(cols) == 7:
            date = cols[0].get_text(strip=True)
            close_price = cols[4].get_text(strip=True)
            print(f"{date} - Close: {close_price}")


if __name__ == "__main__":
    main()