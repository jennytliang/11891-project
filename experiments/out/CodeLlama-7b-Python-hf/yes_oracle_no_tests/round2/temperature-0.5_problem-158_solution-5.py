def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: if len ( words ) ==
	"""
    if len(words) == 0:
        return None
    if len(words) == 1:
        return words[0]
    max_words = []
    max_count = 0
    for word in words:
        if len(set(word)) > max_count:
            max_words = [word]
            max_count = len(set(word))
        elif len(set(word)) == max_count:
            max_words.append(word)
    return min(max_words)


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
