def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt ,
	Do not include these tokens in the code: # for each word in words
	"""
    # Your code here
    m = 0
    ch = ''
    for word in words:
        cnt = 0
        for i in range(len(word)):
            if word.count(word[i]) == 1:
                cnt += 1
        if m < cnt:
            m = cnt
            ch = word
    return ch
