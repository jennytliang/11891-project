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
    max_chars = 0
    max_word = ''
    for word in words:
        chars = set()
        for char in word:
            chars.add(char)
        if len(chars) > max_chars:
            max_chars = len(chars)
            max_word = word
        elif len(chars) == max_chars:
            if word < max_word:
                max_word = word
    return max_word


if __name__ == '__main__':
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb" ,"cc"]))
