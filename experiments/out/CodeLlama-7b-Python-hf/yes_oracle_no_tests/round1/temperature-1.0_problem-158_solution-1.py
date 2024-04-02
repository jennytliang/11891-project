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
    m = {}
    for x in words:
        for ch in x:
            if ch not in m:
                m[ch] = 1
            else:
                m[ch] += 1
    ans = ""
    for x in words:
        cnt = 0
        for ch in x:
            if m[ch] == 1:
                cnt += 1
        if cnt > len(ans):
            ans = x
        elif cnt == len(ans):
            if x < ans:
                ans = x
    return ans


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["", "a", "b"]) == "a"
    assert find_max(["abc", "a", "b"]) == "abc"

if __name__ == '__main__':
    test_function()
