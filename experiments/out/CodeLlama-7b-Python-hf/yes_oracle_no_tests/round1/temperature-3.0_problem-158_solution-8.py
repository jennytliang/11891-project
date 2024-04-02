def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	"""
    max_chars = 0
    ans = ""
    for word in words:
        chars = set(word)
        if len(chars) > max_chars:
            max_chars = len(chars)
            ans = word
        elif len(chars) == max_chars:
            if word < ans:
                ans = word
    return ans


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a", "a", "a"]) == "a"
    assert find_max(["a", "ab", "abc"]) == "abc"
    assert find_max(["abc", "ab", "a"]) == "abc"
    assert find_max(["a", "ab", "ab"]) == "ab"
    assert find_max(["a", "a", "ab"]) == "a"
    assert find_max(["abc", "ab", "ab"]) == "ab"
    assert find_max(["abc", "ab", "abc"]) == "abc"
    assert find_max(["abc", "ab", "abcd"]) == "abcd"
    assert find_max(["abc", "ab", "abcd", "abc"]) == "abc"
    assert find_max(["abc", "ab", "abcd", "abc", "ab"]) == "abc"
    assert find_max(["abc", "ab", "abcd", "abc", "ab", "abc"]) == "abc"
    assert find_max(["abc", "ab", "abcd", "abc", "ab", "abcd"]) == "abcd"
    assert find_max(["abc", "ab", "abcd", "abc", "ab", "abcd", "abc"]) == "abc"
    assert find_max(["abc", "ab", "abcd", "abc", "ab", "abcd",