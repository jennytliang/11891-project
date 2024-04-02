def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: x _ ch _ cnt , ans
	"""

    ans = ""
    cnt = 0
    for x in words:
        ch = set(x)
        if len(ch) > cnt:
            ans = x
            cnt = len(ch)
        elif len(ch) == cnt and x < ans:
            ans = x
    return ans
