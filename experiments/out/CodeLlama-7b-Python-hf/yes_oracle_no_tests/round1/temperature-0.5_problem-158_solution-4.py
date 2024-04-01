def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""

    # Your code here
    m = -1
    _ = ''
    ch = ''
    cnt = 0
    for w in words:
        if len(w) > m:
            m = len(w)
            _ = w
    for ch in _:
        if _.count(ch) > cnt:
            cnt = _.count(ch)
    return _


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
