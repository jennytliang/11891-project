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
    for word in words:
        ch = {}
        for w in word:
            if w in ch:
                ch[w] += 1
            else:
                ch[w] = 1
        m[word] = ch
    ans = ""
    for word in words:
        if len(m[word]) > len(m[ans]):
            ans = word
        elif len(m[word]) == len(m[ans]):
            if word < ans:
                ans = word
    return ans


def test_function(test_case):
    test_input, test_expected = test_case
    function_results = find_max(test_input)
    if function_results == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function((["name", "of", "string"], "string"))
test_function((["name", "enam", "game"], "enam"))
test_function((["aaaaaaa", "bb" ,"cc"], "aaaaaaa"))
test_function((["a", "b", "a", "c", "d"], "a"))
test_function((["a", "a", "a", "b", "b", "b"], "a"))
