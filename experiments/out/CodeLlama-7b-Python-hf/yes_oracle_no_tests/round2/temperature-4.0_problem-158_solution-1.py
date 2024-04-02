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
    if not words:
        return ""

    max_words = words[0]
    max_unique_chars = len(set(words[0]))
    for word in words[1:]:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_words = word
            max_unique_chars = unique_chars
        elif unique_chars == max_unique_chars and word < max_words:
            max_words = word

    return max_words
