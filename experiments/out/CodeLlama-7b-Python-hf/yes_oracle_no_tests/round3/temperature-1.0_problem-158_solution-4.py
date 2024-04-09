def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: # find the max length of
	"""
    if not words:
        return ""

    max_word = words[0]
    max_length = len(set(max_word))

    for word in words:
        if max_length < len(set(word)):
            max_word = word
            max_length = len(set(word))

    return max_word


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a"]) == "a"
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max([]) == ""

