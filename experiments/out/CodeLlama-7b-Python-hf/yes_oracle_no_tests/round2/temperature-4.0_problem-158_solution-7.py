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
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    m = words[0]
    ans = m
    for word in words:
        ch = set()
        for c in word:
            ch.add(c)
        if len(ch) > len(ans):
            ans = word
        elif len(ch) == len(ans):
            if word < ans:
                ans = word
    return ans
