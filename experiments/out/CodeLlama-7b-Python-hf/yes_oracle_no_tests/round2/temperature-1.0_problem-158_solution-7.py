def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # 1 . calculate the number
	"""

    unique_characters = {}
    for word in words:
        for letter in word:
            if letter not in unique_characters:
                unique_characters[letter] = 0
            unique_characters[letter] += 1

    max_unique_characters = 0
    for key in unique_characters:
        if unique_characters[key] > max_unique_characters:
            max_unique_characters = unique_characters[key]

    result = ''
    for word in words:
        if len(unique_characters) == max_unique_characters:
            if word < result:
                result = word
            else:
                result = word

    return result


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["abc", "abc"]) == "abc"
    assert find_max(["abc", "bca"]) == "bca"
    assert find_max(["abc", "cba"]) == "abc"
    assert find_max(["abc", "cab"]) == "abc"
    assert find_max(["abc", "acb"]) == "abc"
    assert find_max(["abc", "ba"]) == "abc"
    assert find_max(["abc", "ab"]) == "abc"
    assert find_max(["abc", "a"]) == "abc"
    assert find_max(["abc", ""]) == "abc"
    assert find_max(["", "a"]) == "a"
    assert find_max(["", ""]) == ""
