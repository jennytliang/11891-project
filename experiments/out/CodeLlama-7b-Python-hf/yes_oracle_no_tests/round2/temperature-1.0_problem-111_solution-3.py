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

    if test == ' ':
        return {}
    else:
        test_list = test.split()
        test_dict = {}


    # Iterate over list, update dict with the key/value pair of the current letter/frequency and convert frequency into int
        count = 1
        for i in test_list:
            if i in test_dict:
                test_dict[i] += 1
            else:
                test_dict[i] = count
            count += 1
                
    # Return dict
        return test_dict
