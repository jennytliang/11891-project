def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Initialize the count for the first
	"""
    words_dict = {}
    for word in words:
        words_dict[word] = len(set(word))
    return max(words_dict, key=words_dict.get)



