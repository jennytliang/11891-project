def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max
	"""
    
    # I didn't come up with this solution and cannot understand it in detail
    max_len = 0
    m = {}
    res = ""
    for word in words:
        if len(word) > max_len:
            m = {}
            max_len = len(word)
            res = word
        
        for c in word:
            if c in m: m[c] += 1
            else: m[c] =1
    
    for w in words:
        if res is w: continue
        tmp = {}
        for c in w:
            if c in tmp: tmp[c] += 1
            else: tmp[c] = 1
        if len(tmp.keys()) > len(m.keys()):
            res = w
        elif len(tmp.keys()) == len(m.keys()):
            if res > w: res = w
    
    return res
 
def find_max_2(words):
    """Write a function that accepts a list of strings. The list contains
    different words. Return the word with maximum number of unique 
    characters. If multiple strings have maximum number of unique 
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max
	"""

    # I've managed to understand how this works now
    # The idea is to iterate through each word
    # Then we collect a dictionary of characters and how often they occur
    # We only count each unique char once
    # Next we create the variable max that will keep track of the length
    # of the string with most unique chars
    # Finally we loop through the dictionary 
    # if the len(dct.keys())>=max then we know that there is a better match
    # so we set a new res