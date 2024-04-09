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
    # find the word with the most unique characters
    # if there are multiple words with the same number of unique characters,
    # return the first word in lexicographical order
    m = -1
    ans = ""
    for word in words:
        ch = set()
        cnt = 0
        for c in word:
            if c not in ch:
                ch.add(c)
                cnt += 1
        if cnt > m:
            m = cnt
            ans = word
        elif cnt == m:
            if word < ans:
                ans = word
    return ans
