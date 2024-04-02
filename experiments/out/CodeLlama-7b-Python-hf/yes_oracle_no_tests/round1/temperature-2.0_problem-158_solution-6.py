def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	Do not include these tokens in the code: if len ( words ) ==
	"""
    ans = ""
    m = 0
    for x in words:
        ch = set()
        cnt = 0
        for i in x:
            if i in ch:
                cnt += 1
            else:
                ch.add(i)
                cnt += 1
        if m < cnt:
            m = cnt
            ans = x
    return ans
