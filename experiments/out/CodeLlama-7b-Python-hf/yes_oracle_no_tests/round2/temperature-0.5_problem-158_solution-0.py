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
    # TODO: Write your code here
    max_word = ""
    max_chars = 0
    for word in words:
        chars = set(word)
        if len(chars) > max_chars:
            max_chars = len(chars)
            max_word = word
        elif len(chars) == max_chars and word < max_word:
            max_word = word
    return max_word


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["name", "of", "string", "of", "string"]) == "string"
    assert find_max(["name", "of", "name"]) == "name"
    assert find_max(["name", "name"]) == "name"
    assert find_max(["of", "of"]) == "of"
    assert find_max(["of"]) == "of"
    assert find_max(["name"]) == "name"
    assert find_max([""]) == ""


if __name__ == '__main__':
    test_function()
