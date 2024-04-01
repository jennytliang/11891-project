def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Include these tokens in the code:  if test == " ": return {}
	Do not include these tokens in the code: pass
	"""

    pass


##############################
# FIRST ATTEMPT
##############################

# def histogram(test):
#     """Given a string representing a space separated lowercase letters, return a dictionary
#     of the letter with the most repetition and containing the corresponding count.
#     If several letters have the same occurrence, return all of them.
    
#     Example:
#     histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
#     histogram('a b b a') == {'a': 2, 'b': 2}
#     histogram('a b c a b') == {'a': 2, 'b': 2}
#     histogram('b b b b a') == {'b': 4}
#     histogram('') == {}

    
#     
#     """
    
#     if test == " ":
#         return {}
#     else:
#         test_list = test.split(" ")
#         test_dict = {}
#         for i in test_list:
#             if i in test_dict:
#                 test_dict[i] += 1
#             else:
#                 test_dict[i] = 1
#         max_value = max(test_dict.values())
#         max_keys = [key for key, value in test_dict.items() if value == max_value]
#         return {key:test_dict[key] for key in max_keys}

##############################
# SECOND ATTEMPT
##############################

# def histogram(test):
#     """Given a string representing a space separated lowercase letters, return a dictionary
#     of the letter with the most repetition and containing the corresponding count.
#     If several letters have the same occurrence, return all of them.
    
#     Example:
#     histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
#     histogram('a b b a') == {'a': 2, 'b': 2}
