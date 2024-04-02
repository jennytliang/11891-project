def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: if not words : return
	"""
    # My solution
    # O(n x m) time | O(m) space
    # m is the number of characters in the longest word
    # n is the number of words
    # The space complexity is O(m) because we are storing the set of characters
    # in each word
    max_word = ""
    max_count = 0
    for word in words:
        word_count = len(set(word))
        if word_count > max_count:
            max_count = word_count
            max_word = word
    return max_word

    # Book solution
    # O(n x m) time | O(m) space
    # m is the number of characters in the longest word
    # n is the number of words
    # The space complexity is O(m) because we are storing the set of characters
    # in each word
    max_word = words[0]
    max_count = len(set(words[0]))
    for word in words:
        word_count = len(set(word))
        if word_count > max_count:
            max_count = word_count
            max_word = word
        elif word_count == max_count:
            if word < max_word:
                max_word = word
    return max_word
