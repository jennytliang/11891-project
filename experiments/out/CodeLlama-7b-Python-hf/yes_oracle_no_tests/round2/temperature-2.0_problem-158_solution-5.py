def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max
	"""
    # your code here
    max_words = []
    for word in words:
        if len(set(word)) > len(max_words):
            max_words = word
        elif len(set(word)) == len(max_words):
            if word < max_words:
                max_words = word
    return max_words


if __name__ == '__main__':
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb", "cc"]))
