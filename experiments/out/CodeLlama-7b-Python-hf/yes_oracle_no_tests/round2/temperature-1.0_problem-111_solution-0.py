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
    d = {}
    if test == " ":
        return {}
    else:
        for i in test:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d2 = {}
        for i in d:
            if d[i] == max(d.values()):
                d2[i] = d[i]
        if len(d2) == 1:
            return d2
        else:
            return d


print(histogram("a b c a b"))
