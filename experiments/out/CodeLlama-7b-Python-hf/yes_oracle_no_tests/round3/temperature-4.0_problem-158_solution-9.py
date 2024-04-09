def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max _ unique
	"""
    if not words:
        return ""
    max_count = 0
    max_word = ""
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_word = word
            max_count = count
    return max_word


def find_max_v2(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max _ unique
	"""
    if not words:
        return ""
    max_count = 0
    max_word = ""
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_word = word
            max_count = count
    return max_word


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["name", "of", "string", "name", "of", "string"]) == "string"
    assert find_max(["name", "of", "string", "name", "of", "string1"]) == "string1"
    assert find_max(["name", "of", "string", "name", "of", "string", "name"]) == "string"
    assert find_max([]) == ""
    assert find_max([""]) == ""
    assert find_