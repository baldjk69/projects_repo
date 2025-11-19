import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("h3 a")
prices = soup.find_all("p", class_="price_color")
data = [
    ["Title", "Price"]
]

for i in range(len(titles)):
    new_price_row = [titles[i]["title"], prices[i].text]
    data.append(new_price_row)
        
with open("book_prices.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)