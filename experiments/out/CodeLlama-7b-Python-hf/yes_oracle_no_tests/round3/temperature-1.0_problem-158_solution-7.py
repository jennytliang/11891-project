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
        if len(word) == 1:
            m[word] = 1
        else:
            for ch in word:
                if ch not in m.keys():
                    m[ch] = 1
                else:
                    m[ch] += 1
    ans = ""
    max_cnt = 0
    for key, val in m.items():
        if val > max_cnt:
            max_cnt = val
            ans = key
    return ans


if __name__ == '__main__':
    words = ["name", "enam", "game"]
    print(find_max(words))
