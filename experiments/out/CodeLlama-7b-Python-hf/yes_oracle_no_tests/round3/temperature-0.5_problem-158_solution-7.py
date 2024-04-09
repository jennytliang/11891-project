def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: #
	"""
    if words == []:
        return ''
    else:
        unique_chars = {}
        for word in words:
            for char in word:
                if char not in unique_chars:
                    unique_chars[char] = 1
                else:
                    unique_chars[char] += 1
        max_unique_chars = max(unique_chars.values())
        for key, value in unique_chars.items():
            if value == max_unique_chars:
                if key < words[0]:
                    return words[0]
                else:
                    return key
        return ''


# TESTS

def test_find_max():
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a", "bb", "cc", "ba"]) == "bb"
    assert find_max(["a", "b", "c", "d", "b"]) == "a"
    assert find_max(["a", "b", "c", "d", "e"]) == "e"
    assert find_max(["a", "b", "c", "d", "e", "f"]) == "f"
    assert find_max(["a", "b", "c", "d", "e", "f", "g"]) == "g"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h"]) == "h"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == "i"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "j"
    assert find_max(["a", "b", "c",