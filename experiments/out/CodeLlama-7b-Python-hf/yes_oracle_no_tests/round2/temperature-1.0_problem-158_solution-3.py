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
    words_dict = {}
    for word in words:
        chars = list(set(word))
        words_dict[word] = len(chars)
        for char in chars:
            chars.sort()
    ans = sorted(words_dict, key = lambda x: (words_dict[x], x))[0]

    return ans


def time_find_max(words, mx):
    assert find_max(words) == mx


def test():
    words = [
        "name","of","string",
        ",","word.","a","aaaa","aaaa","aaaaaaa","bb","cc"
        ]
    mx = "aaaaaaa"
    time_find_max(words, mx)


if __name__ == "__main__":
    test()
