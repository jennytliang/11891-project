def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Initialize the counter for maximum
	"""
    return max(words, key=lambda w: len(set(w)))


# def find_max(words):
#     """Write a function that accepts a list of strings.
#     The list contains different words. Return the word with maximum number
#     of unique characters. If multiple strings have maximum number of unique
#     characters, return the one which comes first in lexicographical order.

#     find_max(["name", "of", "string"]) == "string"
#     find_max(["name", "enam", "game"]) == "enam"
#     find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
# 	Do not include these tokens in the code: # Initialize the counter for maximum
# 	"""
#     unique_chars = set()
#     for word in words:
#         unique_chars = unique_chars | set(word)
#     max_length = 0
#     for word in words:
#         if len(set(word)) == len(unique_chars):
#             if len(word) > max_length:
#                 max_length = len(word)
#     for word in words:
#         if len(word) == max_length:
#             return word
