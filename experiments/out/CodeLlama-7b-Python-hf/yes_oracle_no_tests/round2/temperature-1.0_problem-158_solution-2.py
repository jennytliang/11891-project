def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt ,
	Do not include these tokens in the code: d = {}
	"""
    # check for blank case first
    if len(words) == 0:
        return ''

    first_word = words[0]
    for word in words[1:]:

        # unique characters
        if len(set(first_word)) < len(set(word)):
            first_word= word

        # unique characters equal to first_word
        if len(set(first_word)) == len(set(word)): 

            # first order (ascending order)
            if first_word > word:
                first_word= word

    return first_word
