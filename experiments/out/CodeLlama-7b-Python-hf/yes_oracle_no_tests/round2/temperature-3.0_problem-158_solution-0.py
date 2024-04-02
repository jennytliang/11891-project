def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Your code here
	"""
    if len(words) == 0:
        return None
    elif len(words) == 1:
        return words[0]
    else:
        for i in range(len(words)):
            if len(words[i]) == 1:
                return words[i]
        max_length = 0
        for i in range(len(words)):
            if len(words[i]) > max_length:
                max_length = len(words[i])
                max_index = i
        for i in range(max_index):
            if len(words[i]) == max_length:
                return words[i]
        return words[max_index]
