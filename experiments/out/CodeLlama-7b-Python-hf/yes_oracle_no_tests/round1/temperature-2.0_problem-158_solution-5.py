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
    max_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_word = word
            max_length = len(word)
        elif len(word) == max_length:
            if word < max_word:
                max_word = word
    return max_word


def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"


if __name__ == '__main__':
    test_find_max()
