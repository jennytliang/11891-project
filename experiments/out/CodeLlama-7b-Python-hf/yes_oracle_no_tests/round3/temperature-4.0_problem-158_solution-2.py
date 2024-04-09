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
    # your code here
    m, ans = -1, ''
    for ch in words:
        cnt = len(set(ch))
        if cnt > m:
            m = cnt
            ans = ch
        elif cnt == m:
            ans = min(ans, ch)
    return ans
