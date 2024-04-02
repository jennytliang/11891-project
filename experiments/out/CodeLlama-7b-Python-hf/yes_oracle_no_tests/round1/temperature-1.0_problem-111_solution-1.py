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
    result = {}
    temp = {}
    
    for letter in test:
        if letter not in temp:
            temp[letter] = 1
        else:
            temp[letter] = temp[letter] + 1
    for key, val in temp.items():
        result[key] = temp[key]
        if result[key] > test.count(key):
            result[key] = test.count(key)
    return max(result, key = result.get)