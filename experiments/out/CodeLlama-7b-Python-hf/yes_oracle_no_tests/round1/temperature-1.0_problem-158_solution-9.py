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

    if not words or len(words) == 0:
        return 
        
    m = words[0]
    for x in words:
        cnt = len(set(x))
        if len(m) == cnt or (len(m) > cnt and m > x) or len(m) < cnt and m < x:
            m = x
    
    return m

