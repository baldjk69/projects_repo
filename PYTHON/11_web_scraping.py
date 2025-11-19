import requests
from bs4 import BeautifulSoup
'''
# 1. Fetch the web page
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Check if the request worked
print(response.status_code)

# 2. Parse HTML with BeaitifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3. Extract specific elements
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for i in range(len(quotes)):
    print(f"{quotes[i].text} - {authors[i].text}")


# 4. Extract Tags or Links
for link in soup.find_all("a"):
    print(link.get("href"))

# 5. Save the Scraped Data
with open("quotes.txt", "w", encoding="utf-8") as f: 
    for i in range(len(quotes)):
        f.write(f"{quotes[i].text} - {authors[i].text}\n")
'''
# Example: Scraping News Headlines
url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

for h in headlines[:10]:
    print("📰", h.text.strip())
    
'''
# Error handling
import time
from requests.exceptions import RequestException

try:
   response = requests.get(url)
   response.raise_for_status()

except RequestException as e:
   print("Error fetching page:", e)

time.sleep(1)
'''

