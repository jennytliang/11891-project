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
    ans = ""
    for word in words:
        w = {}
        for ch in word:
            if ch in w:
                w[ch] += 1
            else:
                w[ch] = 1
        if len(w) > len(m):
            m = w
            ans = word
        elif len(w) == len(m):
            if word < ans:
                m = w
                ans = word
    return ans


if __name__ == '__main__':
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb" ,"cc"]))
