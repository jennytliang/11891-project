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
    test_dict = {}
    for i in test:
        if i in test_dict:
            test_dict[i] += 1
        else:
            test_dict[i] = 1
    return test_dict


def histogram_2(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
    """
    test_dict = {}
    for i in test.split(" "):
        if test_dict.get(i):
            test_dict[i] += 1
        else:
            test_dict[i] = 1
    return test_dict


print(histogram("a b c"))
print(histogram("a b b a"))
print(histogram("a b c a b"))
print(histogram("b b b b a"))
print(histogram(""))
print(histogram("a b a b c a b c a b"))


print(histogram_2("a b c"))
print(histogram_2("a b b a"))
print(histogram_2("a b c a b"))
print(histogram_2("b b b b a"))
print(histogram_2(""))
print(histogram_2("a b a b c a b c a b"))
