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
    longest_length = -1                                    # no letters (minumum value)
    result = ""                                           

    for word in words:
        word_length = len({char: 0 for char in word}.keys()) # O(N)

        # if string has more unique characters than the longest string
        # found before: set it as the longest string
        if word_length > longest_length:
            result = word # O(1) 
            longest_length = word_length    # O(1)

    return result # O(1) 


if __name__ == '__main__':
    # Tests for find_max
    assert find_max(["string", "test", "cat"]) == "string"
    assert find_max(["f", "a", "b", "b", "c"]) == "f"
    assert find_max(["name", "of1", "the", "game"]) == "the"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["name", "name", "name"]) == "name"
