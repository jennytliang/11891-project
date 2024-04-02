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

    
	Include these tokens in the code: if test == " ": return {}
	"""
    test = test.split()
    test_dict = {}
    for i in test:
        if i in test_dict:
            test_dict[i] += 1
        else:
            test_dict[i] = 1
    return test_dict


def histogram_max_count(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return the one that appears first in the input string.
    
    Example:
    histogram_max_count('a b c') == {'a': 1}
    histogram_max_count('a b b a') == {'b': 2}
    histogram_max_count('a b c a b') == {'a': 2}
    histogram_max_count('b b b b a') == {'b': 4}
    histogram_max_count('') == {}

    
	Include these tokens in the code: if test == " ": return {}
	"""
    test = test.split()
    test_dict = {}
    for i in test:
        if i in test_dict:
            test_dict[i] += 1
        else:
            test_dict[i] = 1
    max_count = max(test_dict.values())
    test_dict_max = {}
    for k, v in test_dict.items():
        if v == max_count:
            test_dict_max[k] = v
    return test_dict_max


def histogram_max_count_unique(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return the one that appears first in the input string.
    
    Example:
    histogram_max_count_unique('a b c') == {'a': 1}
    histogram_max_count_unique('a b b a') == {'b': 2}
