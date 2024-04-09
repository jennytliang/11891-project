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
    # Your code here
    max_word = ""
    max_count = 0
    for word in words:
        if len(word) > max_count:
            max_count = len(word)
            max_word = word
        elif len(word) == max_count:
            if word < max_word:
                max_word = word
    return max_word


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["a", "b", "c", "d"]) == "a"
    assert find_max(["a", "ab", "abc", "abcd"]) == "abcd"
    assert find_max(["abc", "abcd", "cd", "efg"]) == "abc"
    assert find_max(["abc", "abcd", "cd", "efg", "cd"]) == "cd"
    assert find_max(["abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "