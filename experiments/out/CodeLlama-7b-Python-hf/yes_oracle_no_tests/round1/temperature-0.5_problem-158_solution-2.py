def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""

    # 1. find the longest word in the list
    # 2. find the number of unique characters in the longest word
    # 3. return the word with maximum number of unique characters

    # 1.
    longest_word = find_longest(words)

    # 2.
    unique_count = len(set(longest_word))

    # 3.
    max_word = longest_word
    for word in words:
        if len(word) == len(longest_word):
            if len(set(word)) > unique_count:
                max_word = word

    return max_word


def find_longest(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def find_max_v2(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""
    # 1. find the longest word in the list
    # 2. find the number of unique characters in the longest word
    # 3. return the word with maximum number of unique characters

    # 1.
    longest_word = find_longest(words)

    # 2.
    unique_count = len(set(longest_word))

    # 3.
    max_word = longest_word
    for word in words:
        if len(word) == len(longest_word):