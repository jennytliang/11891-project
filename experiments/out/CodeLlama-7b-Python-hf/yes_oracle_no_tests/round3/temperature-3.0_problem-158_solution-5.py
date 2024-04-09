def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: # TODO : Write your solution
	"""

    max_word = ""
    max_unique = 0
    for word in words:
        unique = set(word)
        if len(unique) > max_unique:
            max_unique = len(unique)
            max_word = word
    return max_word


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["a", "ab", "abc"]) == "abc"
    assert find_max(["a", "abb", "ab"]) == "abb"
    assert find_max(["a", "abbb", "ab"]) == "abbb"
    assert find_max(["a", "abb", "abbb"]) == "abb"
    assert find_max(["abc", "abcd", "abcde"]) == "abcde"
    assert find_max(["abc", "abcd", "abcdef"]) == "abcdef"
