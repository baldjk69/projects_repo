import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

# Adding a user agent(some sites block default Python requests)
headers = {"User-Agent":"Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("h3 a")
prices = soup.find_all("p", class_="price_color")

data = [["Title", "Price"]]
file_path = "(9-12) Python Applied & Git/11_book_prices.csv"

# ZIP for FOR LOOP ITERATION (Avoids index errors)
for title, price in zip(titles, prices):
    row = [title["title"], price.text.decode("utf-8")]
    data.append(row)

# Encode CSV to UTF-8(some book titles contain special characters)     
with open(file_path, "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Add a success message
print("Data saved to book_prices.csv")