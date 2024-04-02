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
    test_list = test.split()
    test_dict = {}
    for i in test_list:
        if i not in test_dict:
            test_dict[i] = test_list.count(i)
    return test_dict


print(histogram("a b c"))
print(histogram("a b b a"))
print(histogram("a b c a b"))
print(histogram("b b b b a"))
print(histogram(""))
print(histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z"))
