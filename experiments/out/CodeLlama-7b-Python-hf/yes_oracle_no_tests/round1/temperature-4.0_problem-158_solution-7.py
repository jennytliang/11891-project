def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: longest
	"""
    # Your code here
    # raise NotImplementedError()
    # pass
    max_word = words[0]
    max_length = len(set(words[0]))
    for word in words:
        if len(set(word)) > max_length:
            max_word = word
            max_length = len(set(word))
    return max_word


if __name__ == '__main__':
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb" ,"cc"]))
