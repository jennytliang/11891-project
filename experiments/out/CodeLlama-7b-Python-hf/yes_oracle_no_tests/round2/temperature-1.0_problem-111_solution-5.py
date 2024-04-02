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
    # write your code here
    if test == " ":
        return {}
    histogram = {}
    for i in test.split():
        histogram[i] = histogram.get(i,0) + 1
    return histogram


def test_function():
    assert histogram("test") == {'t': 1, 'e': 1, 's': 1, 't': 1}
    assert histogram("") == {}
    assert histogram("a b c a b") == {'a': 2, 'b': 2}
    assert histogram("a b c d e a b") == {'a': 2, 'b': 2}
    assert histogram("a a a a b b b b") == {'a': 4, 'b': 4}
    assert histogram("") == {}
