def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _
	Do not include these tokens in the code: # My solution #
	"""
    max_word = words[0]
    max_count = 0

    for word in words:
        count = len(set(word))
        if count > max_count:
            max_word = word
            max_count = count

    return max_word


def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["a", "aa", "aaa"]) == "aaa"
    assert find_max(["string", "stringer", "stringest"]) == "stringest"
    assert find_max(["string", "stringer", "stringest", "stringesting"]) == "stringest"


if __name__ == '__main__':
    test_find_max()
