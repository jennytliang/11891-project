def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: if len ( words ) ==
	"""
    max_words = []
    for word in words:
        if word not in max_words:
            max_words.append(word)
    max_words.sort()
    max_words_unique = []
    for word in max_words:
        if word not in max_words_unique:
            max_words_unique.append(word)
    max_words_unique.sort(key=lambda x: len(set(x)))
    return max_words_unique[-1]


print(find_max(['name', 'of', 'string']))
print(find_max(['name', 'enam', 'game']))
print(find_max(['aaaaaaa', 'bb', 'cc']))
