import re
import string
from collections import Counter

words = []

# read the text file, clean and filter tokens, and keep words with at least two letters in them

with open("sample-file.txt", "r", encoding="utf-8", errors="ignore") as f:
    for w in f.read().split():
        w = w.lower().strip(string.punctuation)
        if len(re.findall(r"[a-zA-Z]", w)) >= 2:
            words.append(w)

bigrams = []
for i in range(len(words) - 1):
    bigrams.append(words[i] + " " + words[i + 1])

counts = Counter(bigrams)

for bg, count in counts.most_common(5):
    print(bg, "->", count)
