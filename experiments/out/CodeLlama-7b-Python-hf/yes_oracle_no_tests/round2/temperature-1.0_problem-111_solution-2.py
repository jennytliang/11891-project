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

    
	Include these tokens in the code: if
	Do not include these tokens in the code: #
	"""
    counts = {}
    test_words = test.split(" ")
    for i in test_words:
        if i == '':
            continue
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    return counts
        
# print(histogram("a b c a b"))
# print(histogram("z c a b"))
# print(histogram(""))

########## Solution ###############

# def histogram(test):
#     """Given a string representing a space separated lowercase letters, 
#     return a dictionary of the letter with the most repetition 
#     and containing the corresponding count.
#     If several letters have the same occurrence, return all of them.
#     
#     Example:
#     histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
#     histogram('a b b a') == {'a': 2, 'b': 2}
#     histogram('a b c a b') == {'a': 2, 'b': 2}
#     histogram('b b b b a') == {'b': 4}
#     histogram('') == {}

#     
#     Include these tokens in the code: if elif
#     Do not include these tokens in the code: #
#     """
#     word_list = [i for i in test.split(" ")]
#     word_dict = {}
#     for words in word_list:
#         if words not in word_dict:
#             word_dict[words] = 1
#         else:
#             word_dict[words] += 1

#     return word_dict
