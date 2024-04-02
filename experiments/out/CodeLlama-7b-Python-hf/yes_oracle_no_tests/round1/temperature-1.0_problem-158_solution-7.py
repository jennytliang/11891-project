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
    # 1. calculate the number of unique characters in each word
    # 2. find the maximum number of unique characters
    # 3. find the word with the maximum number of unique characters
    # 4. return the word with the maximum number of unique characters
    m = {}
    ans = ""
    for w in words:
        ch_cnt = {}
        for ch in w:
            if ch not in ch_cnt:
                ch_cnt[ch] = 0
            ch_cnt[ch] += 1
        m[w] = ch_cnt

    for w in words:
        if len(m[w]) > len(m[ans]):
            ans = w
        elif len(m[w]) == len(m[ans]):
            if w < ans:
                ans = w
    return ans

def find_max_test():

    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["a", "a", "a"]) == "a"
    print("Test succeeded.")

if __name__ == "__main__":

    find_max_test()
