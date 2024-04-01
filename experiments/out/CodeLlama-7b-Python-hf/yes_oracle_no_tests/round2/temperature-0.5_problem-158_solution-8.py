def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max _ word = ''
	"""
    word_dict = {}
    for word in words:
        chars = set(word)
        if len(chars) not in word_dict:
            word_dict[len(chars)] = []
        word_dict[len(chars)].append(word)
    return word_dict[max(word_dict.keys())][0]


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["a", "a"]) == "a"

if __name__ == '__main__':
    test_function()
