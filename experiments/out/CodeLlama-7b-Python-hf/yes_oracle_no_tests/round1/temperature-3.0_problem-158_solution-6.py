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
    ans = ''
    for ch in words[0]:
        m[ch] = 1

    for word in words:
        for ch in word:
            m[ch] += 1
        if len(m) > len(ans):
            ans = word
        elif len(m) == len(ans):
            if word < ans:
                ans = word
    return ans


def test_function(test_case):
    test_input, test_expected = test_case
    test_actual = find_max(test_input)
    if test_actual == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function((["name", "of", "string"], "string"))
test_function((["name", "enam", "game"], "enam"))
test_function((["aaaaaaa", "bb", "cc"], "aaaaaaa"))
test_function((["ab", "a"], "ab"))
