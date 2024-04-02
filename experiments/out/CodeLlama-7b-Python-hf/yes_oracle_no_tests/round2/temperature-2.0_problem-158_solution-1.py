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
    # print(words)
    m = 0
    ans = ''
    for i in words:
        ch = set(i)
        if len(ch) > m:
            m = len(ch)
            ans = i
        elif len(ch) == m:
            if i < ans:
                ans = i
    return ans


find_max(["name", "of", "string"])
