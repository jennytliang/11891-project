def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt ,
	"""
    if not words:
        return ""
    max_chars = 0
    max_str = words[0]
    for word in words:
        if len(set(word)) > max_chars:
            max_chars = len(set(word))
            max_str = word
    return max_str
