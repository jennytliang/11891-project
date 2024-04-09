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
    m = {}
    for word in words:
        ch = set()
        for letter in word:
            ch.add(letter)
        m[word] = len(ch)
    ans = max(m, key=m.get)
    return ans


def find_max_2(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"

    Include these tokens in the code: m x _ ch _ cnt , ans =
    """
    m = {}
    for word in words:
        ch = set()
        for letter in word:
            ch.add(letter)
        if len(ch) not in m:
            m[len(ch)] = word
        elif len(ch) in m and word < m[len(ch)]:
            m[len(ch)] = word
    ans = max(m, key=m.get)
    return m[ans]
