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
    # init
    m = 0
    ans = ''
    # traverse
    for ch in words:
        # init
        cnt = 0
        # traverse
        for i in ch:
            if ch.count(i) == 1:
                cnt += 1
        # update
        if cnt > m:
            m = cnt
            ans = ch
    return ans


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["a"]) == "a"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == "abc"
    assert find_max(["aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa"]) == "aaaaaaa"
    assert find_max(["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc",