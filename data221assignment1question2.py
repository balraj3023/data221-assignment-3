def build_string_dictionary(strings):
    result = {}

    for word in strings:
        length = len(word)

        if length % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        result[word] = {
            "length": length,
            "parity": parity
        }

    return result

strings = ["data", "science"]
output = build_string_dictionary(strings)

print(output)




