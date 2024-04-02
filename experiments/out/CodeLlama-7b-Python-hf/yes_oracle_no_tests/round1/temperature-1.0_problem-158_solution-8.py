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
    res = ''
    for w in words:
        temp_cnt = {}
        for c in w:
            if c not in temp_cnt:
                temp_cnt[c] = 1
            else:
                temp_cnt[c] += 1
        if len(temp_cnt.keys()) > len(res):
            res = w
    return res

