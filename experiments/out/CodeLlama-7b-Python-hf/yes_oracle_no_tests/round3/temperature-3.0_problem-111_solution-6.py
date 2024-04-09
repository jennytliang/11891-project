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

    
	Include these tokens in the code: count , ans
	Do not include these tokens in the code: test _ list
	"""


    if test == "":
        ret = {}
    else:
        test_list = test.split(" ")
        ret = {}
        for i in test_list:
            if i in ret:
                ret[i] += 1
            else:
                ret[i] = 1
        if len(ret) == 1:
            ret = ret[0]
    return ret

print(histogram("a b b b a"))
