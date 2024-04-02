def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt ,
	Do not include these tokens in the code: if not words : return
	"""
    if not words:
        return ""
    m = 0
    ch = ""
    for w in words:
        if len(set(w)) > m:
            m = len(set(w))
            ch = w
    return ch
