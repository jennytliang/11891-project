def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: longest
	"""
    # your code here
    words_unique_characters = {}
    for word in words:
        unique_characters = set(word)
        words_unique_characters[word] = len(unique_characters)

    max_value = max(words_unique_characters.values())
    words_max = [word for word, length in words_unique_characters.items() if length == max_value]
    return min(words_max)
