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
    max_unique = 0
    ans = ""
    for word in words:
        unique = 0
        for ch in word:
            if word.count(ch) == 1:
                unique += 1
        if unique > max_unique:
            max_unique = unique
            ans = word
    return ans
