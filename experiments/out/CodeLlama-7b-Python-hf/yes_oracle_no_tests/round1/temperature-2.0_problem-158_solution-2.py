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
    m = 0
    ans = ""
    for word in words:
        ch = set()
        for i in word:
            if i in ch:
                break
            ch.add(i)
        if len(ch) > m:
            m = len(ch)
            ans = word
    return ans


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
