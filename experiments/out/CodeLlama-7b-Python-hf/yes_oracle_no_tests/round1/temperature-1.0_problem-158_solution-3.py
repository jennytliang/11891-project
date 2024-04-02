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
    words_sorted = ""

    for i in words:
        if i != words_sorted and i.count(i[0]) == 1:
            words_sorted = i
            
    return words_sorted
    # return max(set(words), key=words.count)


def test_find_max():
    assert find_max([ "name", "of", "string" ]) == "string"
    assert find_max([ "name", "enam", "game" ]) == "enam"
    assert find_max([ "aaaaaaa", "bb", "cc"]) == "aaaaaaa"
