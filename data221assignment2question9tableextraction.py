import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}

# Download page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Main content area
content = soup.find("div", id="mw-content-text")

# locate the first table with at least 3 data rows
target_table = None
for table in content.find_all("table"):
    data_rows = 0
    for tr in table.find_all("tr"):
        if tr.find_all("td"):
            data_rows += 1
    if data_rows >= 3:
        target_table = table
        break

if target_table is None:
    print("No table with at least 3 data rows found.")
    raise SystemExit

rows = target_table.find_all("tr")

# determine the maximum number of columns across rows
max_cols = 0
for tr in rows:
    cells = tr.find_all(["th", "td"])
    if len(cells) > max_cols:
        max_cols = len(cells)

first_row_th = rows[0].find_all("th")

if len(first_row_th) > 0:
    headers_list = [th.get_text(" ", strip=True) for th in first_row_th]
else:
    headers_list = []

if len(headers_list) == 0:
    headers_list = ["col" + str(i + 1) for i in range(max_cols)]
else:
    while len(headers_list) < max_cols:
        headers_list.append("col" + str(len(headers_list) + 1))

# extract rows, pad missing values with empty strings
data = []
for tr in rows[1:]:
    cells = tr.find_all(["td", "th"])
    if len(cells) == 0:
        continue

    values = [c.get_text(" ", strip=True) for c in cells]

    while len(values) < len(headers_list):
        values.append("")

    values = values[:len(headers_list)]
    data.append(values)

# save to CSV
df = pd.DataFrame(data, columns=headers_list)
df.to_csv("wiki_table.csv", index=False)

print("Saved wiki_table.csv")
print("Columns:", len(headers_list))
print("Rows:", len(df))


