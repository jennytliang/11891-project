def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Your code here #
	"""

    # Your code here
    def find_max_helper(words, word_dict):
        if len(words) == 0:
            return word_dict
        else:
            curr_word = words[0]
            new_word_dict = word_dict
            if len(curr_word) > len(new_word_dict[0][1]):
                new_word_dict = [(curr_word, curr_word)]
            return find_max_helper(words[1:], new_word_dict)

    return find_max_helper(words, [(words[0], words[0])])[0]


def find_max_v2(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Your code here #
	"""

    # Your code here
    def find_max_helper(words, word_dict):
        if len(words) == 0:
            return word_dict
        else:
            curr_word = words[0]
            new_word_dict = word_dict
            if len(curr_word) > len(new_word_dict[0][1]):
                new_word_dict = [(curr_word, curr_word)]
            return find_max_helper(words[1:], new_word_dict)

    return find_max_helper(words, [(words[0], words[0])])[0]


def find_max_v3(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters.