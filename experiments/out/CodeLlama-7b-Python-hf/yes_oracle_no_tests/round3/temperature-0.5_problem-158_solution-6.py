def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: #
	"""
    def get_charset(word):
        charset = set()
        for char in word:
            charset.add(char)
        return charset

    max_word = None
    max_charset = set()
    for word in words:
        if len(get_charset(word)) > len(max_charset):
            max_charset = get_charset(word)
            max_word = word
        elif len(get_charset(word)) == len(max_charset):
            if word < max_word:
                max_word = word
    return max_word


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
