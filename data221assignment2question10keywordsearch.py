def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    keyword (case-insensitive). Line numbers start at 1.
    """
    results = []

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        line_num = 1
        for line in f:
            if keyword.lower() in line.lower():
                results.append((line_num, line.rstrip("\n")))
            line_num += 1

    return results

# test with sample-file.txt and use the keyword "lorem"
matches = find_lines_containing("sample-file.txt", "lorem")

print("Matching lines found:", len(matches))
print()

