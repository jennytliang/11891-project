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

    # m x _ ch _ cnt , ans =
    m = 0
    ans = ""
    for word in words:
        ch = set()
        cnt = 0
        for ch in word:
            if ch not in ch:
                ch.add(ch)
                cnt += 1
        if cnt > m:
            m = cnt
            ans = word
        elif cnt == m:
            if word < ans:
                ans = word
    return ans


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
    # m x _ ch _ cnt , ans =
    m = 0
    ans = ""
    for word in words:
        ch = set()
        cnt = 0
        for ch in word:
            if ch not in ch:
                ch.add(ch)
                cnt += 1
        if cnt > m:
            m = cnt
            ans = word
        elif cnt == m:
            if word < ans:
                ans = word
    return ans


def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
