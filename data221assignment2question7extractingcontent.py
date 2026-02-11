import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print("Title:")
print(soup.title.text)
print()

# find main content
content = soup.find("div", id="mw-content-text")

# find the first paragraph with at least 50 characters
for p in content.find_all("p"):
    text = p.text.strip()
    if len(text) >= 50:
        print("First paragraph:")
        print(text)
        break

