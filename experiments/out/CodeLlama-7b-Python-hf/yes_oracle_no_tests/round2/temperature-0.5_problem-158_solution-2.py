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
    if not words:
        return ''
    ans = ''
    m = {}
    for word in words:
        for ch in word:
            if ch not in m:
                m[ch] = 0
            m[ch] += 1
        if len(m) > len(ans):
            ans = word
        elif len(m) == len(ans) and word < ans:
            ans = word
        m = {}
    return ans


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
