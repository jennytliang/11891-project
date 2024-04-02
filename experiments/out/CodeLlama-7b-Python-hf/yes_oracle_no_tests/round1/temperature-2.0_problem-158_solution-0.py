def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	Do not include these tokens in the code: if len ( words ) ==
	"""
    # Your code here
    m = 0
    ans = ''
    for _ch in set(''.join(words)):
        cnt = 0
        for _word in words:
            if _ch in _word:
                cnt += 1
        if cnt > m:
            m = cnt
            ans = _ch

    return ans
