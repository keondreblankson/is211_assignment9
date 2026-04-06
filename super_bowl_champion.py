# super_bowl_champions.py
# Scrapes the Super Bowl champions table from Wikipedia
# URL: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions

import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"


def main():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the main "Super Bowl championships" table
    tables = soup.find_all("table", class_="wikitable")
    if not tables:
        print("No Wikipedia tables found.")
        return

    target_table = tables[0]
    rows = target_table.find_all("tr")

    # Print header
    print("Game | Date | Winning Team | Score | Losing Team")
    print("-" * 70)

    for row in rows[1:]:
        cols = row.find_all(["th", "td"])
        text_cols = [col.get_text(" ", strip=True) for col in cols]

        # We only want rows that look like actual game entries
        if len(text_cols) >= 5:
            game = text_cols[0]
            date = text_cols[1]
            winner = text_cols[2]
            score = text_cols[3]
            loser = text_cols[4]

            print(f"{game} | {date} | {winner} | {score} | {loser}")


if __name__ == "__main__":
    main()