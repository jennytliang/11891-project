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

    """
    # Write your function here.
    return_dict = {}
    if len(test) == 0:
    	return return_dict
    max_rep = 0
    char_rep = ' '
    for char in set(test.lower().split(" ")):
    	counter = test.lower().count(char)
    
    	return_dict[char] = counter 
    
    # return return_dict