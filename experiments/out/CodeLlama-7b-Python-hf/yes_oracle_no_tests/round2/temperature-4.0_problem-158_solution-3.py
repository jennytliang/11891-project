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
    # initialize the counter
    m = 0
    # initialize the answer
    ans = ""
    # loop through the list
    for x in words:
        # initialize a counter for this word
        cnt = 0
        # loop through the word
        for ch in x:
            # if the character is not already in the answer
            if ch not in ans:
                # count it
                cnt += 1
        # if the word has more unique characters than the current answer
        if cnt > m:
            # update the answer
            ans = x
            # update the count
            m = cnt
    # return the answer
    return ans


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["name", "name", "name"]) == "name"
    assert find_max(["abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "bca", "cab"]) == "bca"
    assert find_max(["abc", "cba", "bac"]) == "bac"
    assert find_max(["abc", "cba", "ab"]) == "abc"
    assert find_max(["abc", "cba", "ba"]) == "ba"
    assert find_max(["abc", "cba", "cba"]) == "cba"
    assert find_max(["abc", "cba", "cba", "cba"]) == "cba"

if __name__ == '__main__':
    test_function()
