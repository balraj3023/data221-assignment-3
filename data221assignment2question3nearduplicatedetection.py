import os

def normalize(line):
    line = line.lower()
    cleaned = ""
    for ch in line:
        # keep only letters and numbers
        if ch.isalnum():
            cleaned += ch
    return cleaned

groups = {}

with open("sample-file.txt", "r", encoding="utf-8", errors="ignore") as f:
    line_num = 1
    for line in f:
        key = normalize(line)

        # skip lines that become blank
        if key == "":
            line_num += 1
            continue

        if key not in groups:
            groups[key] = []

        groups[key].append((line_num, line.rstrip("\n")))
        line_num += 1

# collect near-duplicate sets (2 or more lines)
dup_sets = []
for key in groups:
    if len(groups[key]) >= 2:
        dup_sets.append(groups[key])

print("Number of near-duplicate sets:", len(dup_sets))
print()

# print the first two sets
for i in range(min(2, len(dup_sets))):
    print("Set", i + 1)
    for num, text in dup_sets[i]:
        print(str(num) + ":", text)
    print()

