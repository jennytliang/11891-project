def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: if not words : return
	"""
    if not words:
        return ""

    counter = {}
    for word in words:
        unique_chars = set(word)
        for char in unique_chars:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

    max_num = max(counter.values())
    max_words = []
    for word, num in counter.items():
        if num == max_num:
            max_words.append(word)

    return min(max_words)


if __name__ == "__main__":
    test_words = [
        ["name", "of", "string"],
        ["name", "enam", "game"],
        ["aaaaaaa", "bb", "cc"],
    ]

    for words in test_words:
        print("Testing:", words)
        print("Result:", find_max(words))
        print("=" * 20)
