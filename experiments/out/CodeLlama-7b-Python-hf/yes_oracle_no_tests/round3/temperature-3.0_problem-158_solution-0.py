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
    # m x _ ch _ cnt , ans =
    ans = ""
    m = 0
    for x in words:
        ch = set()
        for i in x:
            if i not in ch:
                ch.add(i)
        if m < len(ch):
            ans = x
            m = len(ch)
    return ans


def test_function(test_case):
    test_input, test_expected = test_case
    if find_max(test_input) == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function((["name", "of", "string"], "string"))
test_function((["name", "enam", "game"], "enam"))
test_function((["aaaaaaa", "bb", "cc"], "aaaaaaa"))
test_function((["aabb", "ab", "a"], "aabb"))
test_function((["a", "a", "aa"], "aa"))
test_function((["a", "aa", "aaa"], "aaa"))
test_function((["a", "aa", "aaa", "aaaa"], "aaaa"))
test_function((["a", "aa", "aaa", "aaaa", "aaaaa"], "aaaaa"))
test_function((["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], "aaaaaa"))
test_function((["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"], "aaaaaa"))
test_function((["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"], "aaaaaa"))
test_function((["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa"], "aaaaaaa"))
test_function((["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], "aaaaaaaa