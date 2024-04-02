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
    unique_chars = []
    for word in words:
        for char in word:
            if char not in unique_chars:
                unique_chars.append(char)
    max_word = words[0]
    max_index = 0
    for i, word in enumerate(words):
        if len(set(word)) == len(unique_chars):
            if word > max_word:
                max_word = word
                max_index = i
    return words[max_index]


def find_max_solution(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: if len ( words ) ==
	"""
    unique_chars = []
    for word in words:
        for char in word:
            if char not in unique_chars:
                unique_chars.append(char)
    max_word = words[0]
    max_index = 0
    for i, word in enumerate(words):
        if len(set(word)) == len(unique_chars):
            if word > max_word:
                max_word = word
                max_index = i
    return words[max_index]


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
