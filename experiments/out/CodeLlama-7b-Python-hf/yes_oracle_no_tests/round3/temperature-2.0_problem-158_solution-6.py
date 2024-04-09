def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: if not words : return
	"""
    if not words:
        return
    max_word = words[0]
    max_count = len(set(max_word))
    for word in words[1:]:
        if len(set(word)) > max_count:
            max_word = word
            max_count = len(set(word))
        elif len(set(word)) == max_count and word < max_word:
            max_word = word
            max_count = len(set(word))
    return max_word


def find_max_2(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: if not words : return
	"""
    if not words:
        return
    max_word = words[0]
    max_count = len(set(max_word))
    for word in words[1:]:
        if len(set(word)) > max_count:
            max_word = word
            max_count = len(set(word))
        elif len(set(word)) == max_count and word < max_word:
            max_word = word
            max_count = len(set(word))
    return max_word
