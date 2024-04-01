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

    # 1. get max unique characters
    # 2. get the first alphabetically
    # 3. return the first alphabetically

    # get max unique characters
    max_chars = 0
    max_chars_word = ""

    for word in words:
        chars = set()
        for char in word:
            if char not in chars:
                chars.add(char)

        if len(chars) > max_chars:
            max_chars = len(chars)
            max_chars_word = word

    # get the first alphabetically
    first_word = None
    for word in words:
        if word < max_chars_word and first_word is None:
            first_word = max_chars_word

    if first_word is None:
        first_word = max_chars_word

    return first_word


def find_max_no_loops(words):
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

    # 1. get max unique characters
    # 2. get the first alphabetically
    # 3. return the first alphabetically

    # get max unique characters
    max_chars = 0
    max_chars_word = ""

    for word in words:
        chars = set()
        for char in word:
            if char not in chars:
                chars.add(char)

        if len(chars