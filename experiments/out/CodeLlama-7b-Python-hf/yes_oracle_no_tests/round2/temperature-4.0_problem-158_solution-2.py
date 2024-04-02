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
    # Your code here
    m = {}
    for word in words:
        for ch in word:
            if ch in m:
                m[ch] += 1
            else:
                m[ch] = 1
    ans = ""
    max_cnt = -1
    for word in words:
        cnt = 0
        for ch in word:
            cnt += m[ch]
        if cnt > max_cnt:
            ans = word
            max_cnt = cnt
        elif cnt == max_cnt:
            if word < ans:
                ans = word
    return ans
