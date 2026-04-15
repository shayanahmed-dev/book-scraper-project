import requests
from bs4 import BeautifulSoup
import csv

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])

    for i in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("h3")
        prices = soup.find_all("p", class_="price_color")

        for book, price in zip(books, prices):
            writer.writerow([book.find("a")["title"], price.text.strip().encode("latin1").decode("utf-8")])

print("Saved to books.csv!")