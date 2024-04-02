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
    # Your code here
    max_length = 0
    max_string = ""
    for word in words:
        if len(set(word)) > max_length:
            max_length = len(set(word))
            max_string = word
    return max_string


def find_max_v2(words):
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
    # Your code here
    max_length = 0
    max_string = ""
    for word in words:
        if len(set(word)) > max_length:
            max_length = len(set(word))
            max_string = word
    return max_string
