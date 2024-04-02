def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # 1 st br
	"""
    max_unique_chars = -1
    max_string = ""
    for word in words:
        unique_chars = 0
        for char in word:
            if word.count(char) == 1:
                unique_chars += 1
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_string = word
    return max_string


def find_max2(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # 1 st br
	"""
    max_unique_chars = -1
    max_string = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_string = word
    return max_string


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
test_function((["aabb", "cc"], "aabb"))
test_function((["aabb", "d"], "d"))
test_function((["a