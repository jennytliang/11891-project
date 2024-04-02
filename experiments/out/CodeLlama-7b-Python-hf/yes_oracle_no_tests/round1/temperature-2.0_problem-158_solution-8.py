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
    m = {}
    for word in words:
        for ch in word:
            if ch in m:
                m[ch] += 1
            else:
                m[ch] = 1
    ans = ""
    for word in words:
        if len(ans) == 0:
            ans = word
        elif len(m) == len(set(word)):
            if word < ans:
                ans = word
        elif len(m) > len(set(word)):
            ans = word
    return ans
