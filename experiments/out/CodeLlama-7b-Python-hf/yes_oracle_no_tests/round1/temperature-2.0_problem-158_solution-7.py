def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: if len ( words ) ==
	"""
    if not words:
        return

    max_word = words[0]
    max_unique_chars = set(words[0])
    for word in words[1:]:
        unique_chars = set(word)
        if len(unique_chars) > len(max_unique_chars):
            max_word = word
            max_unique_chars = unique_chars
        elif len(unique_chars) == len(max_unique_chars):
            if word < max_word:
                max_word = word
    return max_word


def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["a", "b", "c", "d"]) == "b"
    assert find_max(["a", "b", "c", "d", "e"]) == "c"
    assert find_max(["a", "b", "c", "d", "e", "f"]) == "d"
    assert find_max(["a", "b", "c", "d", "e", "f", "g"]) == "e"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h"]) == "f"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == "g"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "h"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]) == "