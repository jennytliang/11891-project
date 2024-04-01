def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: # 1 . get max
	"""
    # m x
    # 1 . get max
    max_word = words[0]
    max_chars = len(set(max_word))
    for word in words:
        if len(set(word)) > max_chars:
            max_word = word
            max_chars = len(set(word))
    return max_word
