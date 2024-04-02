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
    if len(words) == 0:
        return ""
    m = 0
    ans = ""
    for ch in words[0]:
        m += 1
    for word in words:
        cnt = 0
        for ch in set(word):
            cnt += 1
        if cnt > m:
            m = cnt
            ans = word
        elif cnt == m:
            if word < ans:
                ans = word
    return ans


def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["name", "of", "string", "game"]) == "string"
    assert find_max(["name", "of", "string", "game", "game"]) == "string"
    assert find_max(["name", "of", "string", "game", "game", "game"]) == "game"
    assert find_max(["name", "of", "string", "game", "game", "game", "game"]) == "game"
    assert find_max(["name", "of", "string", "game", "game", "game", "game", "game"]) == "game"
    assert find_max(["name", "of", "string", "game", "game", "game", "game", "game", "game"]) == "game"
    assert find_max(["name", "of", "string", "game", "game", "game", "game", "game", "game", "game"]) == "game"
    assert find_max(["name", "of", "string", "game", "game", "game", "game", "game", "game", "game", "game"]) == "game"
    assert find_max(["name", "of", "string", "game", "game", "game", "game", "game", "game", "game", "game", "game