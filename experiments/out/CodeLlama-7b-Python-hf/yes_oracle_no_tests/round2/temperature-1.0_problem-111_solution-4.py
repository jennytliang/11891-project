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

    if test == '':
        return {}
    else:
        test = test.split()
        histogram = {}
        for i in test:
            histogram[i] = test.count(i)
    return histogram


def histogram_unique(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return only the one with the highest count.
    
    Example:
    histogram_unique('a b c') == {'a': 1}
    histogram_unique('a b b a') == {'b': 1}
    histogram_unique('a b c a b') == {'a': 1}
    histogram_unique('b b b b a') == {'b': 1}
    histogram_unique('') == {}

    Include these tokens in the code:
    """
    if test == '':
        return {}
    else:
        test = test.split()
        histogram = {}
        for i in test:
            histogram[i] = test.count(i)
        histogram = {k: v for k, v in histogram.items() if v == max(histogram.values())}
    return histogram
