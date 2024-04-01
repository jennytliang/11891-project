def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""

    # For each word in words, count the number of unique characters in the word
    # and store it in a dictionary with the word as the key and the number of
    # unique characters as the value
    char_counts = {}

    for word in words:
        char_counts[word] = len(set(word))

    # Find the word with the highest count
    max_word = max(char_counts, key=char_counts.get)

    return max_word


def main():
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb" ,"cc"]))


if __name__ == "__main__":
    main()
