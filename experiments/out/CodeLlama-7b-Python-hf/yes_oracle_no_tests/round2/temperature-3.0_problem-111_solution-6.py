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

    
	Include these tokens in the code: ":
	"""

    if test == "":
        return {}

    test_list = test.split()
    test_dict = {}
    max_occur = 0

    for item in test_list:
        if item not in test_dict:
            test_dict[item] = 1
        else:
            test_dict[item] += 1

        if test_dict[item] > max_occur:
            max_occur = test_dict[item]

    return_dict = {}

    for key, value in test_dict.items():
        if value == max_occur:
            return_dict[key] = value

    return return_dict























