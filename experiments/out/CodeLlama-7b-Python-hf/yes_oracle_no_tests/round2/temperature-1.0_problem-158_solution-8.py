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
    m = {"_": 0, "ch": -1, "cnt": 0 }
    for word in words:
        cnt = len(set(word))
        for i in word:
            m[i] = m[i] + 1 if m[i] > 0 else -1
        if (cnt > m["cnt"] or cnt == m['cnt'] and word > m["ch"]) and cnt != 0:
            m["cnt"] = cnt
            m["ch"] = word

    ans = m["ch"] if m["cnt"] != 0 else ""

    return ans


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
print(find_max(["name", "of", "string1"]))
print(find_max(["name", "of", ""]))
print(find_max(["name", "of"]))
print(find_max([""]))