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
    max_cnt = 0
    ans = ""
    for w in words:
        cnt = 0
        for ch in w:
            if w.count(ch) == 1:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            ans = w
    return ans
