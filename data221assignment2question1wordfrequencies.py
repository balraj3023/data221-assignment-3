import re
import string
from collections import Counter

def clean_tokens(filename):
    tokens = []
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for word in f.read().split():
            word = word.lower().strip(string.punctuation)

            #  only keep the tokens that contain at least two alphabetic characters
            if len(re.findall(r"[a-zA-Z]", word)) >= 2:
                tokens.append(word)
    return tokens

tokens = clean_tokens("sample-file.txt")
counts = Counter(tokens)

for word, count in counts.most_common(10):
    print(f"{word} -> {count}")
