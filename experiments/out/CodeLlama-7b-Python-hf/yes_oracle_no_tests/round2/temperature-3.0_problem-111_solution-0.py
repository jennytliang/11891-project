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

    
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    test_list = test.split(" ")
    count_dict = {}
    for i in test_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


print(histogram("a b c"))
print(histogram("a b b a"))
print(histogram("a b c a b"))
print(histogram("b b b b a"))
print(histogram(""))
