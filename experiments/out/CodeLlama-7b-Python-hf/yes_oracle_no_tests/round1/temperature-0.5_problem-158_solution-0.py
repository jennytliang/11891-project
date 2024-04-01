def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""

    # for word in words:
    #     if len(set(word)) == max(len(set(w)) for w in words):
    #         return word
    # return ""

    # if len(words) == 1:
    #     return words[0]
    #
    # m = max(set(words), key=lambda x: len(set(x)))
    # return m

    return max(words, key=lambda x: (len(set(x)), x))


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_max(["name", "of", "string"]) == "string", "Name"
    assert find_max(["name", "of", "book"]) == "name", "Book"
    assert find_max(["", "a", "ab", "abc", "abcd"]) == "abcd", "Empty"
    assert find_max(["a", "ab", "abc", "abcd", "abcde"]) == "abcde", "Long"
    assert find_max(["a", "ab", "abc", "abcd", "def", "pqrs", "tuv", "xyz"]) == "abcde", "All"
    assert find_max(["a", "ab", "abc", "abcd", "def", "fgh", "xyz", "pqrs", "tuv"]) == "abcde", "All"
    assert find_max(["a", "ab", "abc", "abcd", "defg", "fgh", "xyz", "pqrs", "tuv"]) == "defg", "First"


if __name__ == '__main__':
    test_function()
