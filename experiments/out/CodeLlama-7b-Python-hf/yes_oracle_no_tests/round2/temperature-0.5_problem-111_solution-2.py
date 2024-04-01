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
    return histogram


def test_histogram():
    assert histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}
    assert histogram("a b b a") == {'a': 2, 'b': 2}
    assert histogram("a b c a b") == {'a': 2, 'b': 2}
    assert histogram("b b b b a") == {'b': 4}
    assert histogram("") == {}
    assert histogram(" a b c") == {'a': 1, 'b': 1, 'c': 1}
    assert histogram("a b c ") == {'a': 1, 'b': 1, 'c': 1}
    assert histogram("a b c  a") == {'a': 2, 'b': 1, 'c': 1}
    assert histogram("a b c a b c a b c a b c") == {'a': 4, 'b': 4, 'c': 4}
    assert histogram("a b c a b c a b c a b c a b c a b c a b c") == {'a': 11, 'b': 11, 'c': 11}
    assert histogram(" a b c  a b c  a b c  a b c  a b c  a b c  a b c") == {'a': 11, 'b': 11, 'c': 11}
    assert histogram("a b c a b c a b c a b c a b c a b c a b c a b c") == {'a': 11, 'b': 11, 'c': 11}
    assert histogram("a b c a b c a b c a b c a b c a b c a b c a b c a b c") == {'a': 11, 'b': 11, 'c': 11}
    assert histogram("a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c") ==