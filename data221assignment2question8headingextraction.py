import requests
from bs4 import BeautifulSoup

webpage = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(webpage, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", id="mw-content-text")

bad_words = ["references", "external links", "see also", "notes"]
headings = []

for h2 in content.find_all("h2"):
    text = h2.get_text().strip()

    # remove [edit]
    text = text.replace("[edit]", "").strip()

    # skip unwanted headings
    lower = text.lower()
    skip = False
    for w in bad_words:
        if w in lower:
            skip = True
            break

    if not skip and text != "":
        headings.append(text)

# save to headings.txt
with open("headings.txt", "w", encoding="utf-8") as f:
    for h in headings:
        f.write(h + "\n")

print("Saved", len(headings), "headings to headings.txt")
