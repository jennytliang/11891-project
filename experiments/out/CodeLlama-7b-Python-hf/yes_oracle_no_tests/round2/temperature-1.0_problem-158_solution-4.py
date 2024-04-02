def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt ,
	"""

    # find the max length of the words
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    # print(max_length)

    # create a dict with the words as keys and the count of unique characters as values
    word_count = {}
    for word in words:
        word_count[word] = len(set(word))

    # return the word with the maximum unique characters
    for word in words:
        if word_count[word] == max_length:
            return word
