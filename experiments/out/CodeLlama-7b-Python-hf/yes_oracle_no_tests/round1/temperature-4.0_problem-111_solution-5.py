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
    pass


def histogram_list(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram_list('a b c') == ['a', 'b', 'c']
    histogram_list('a b b a') == ['a', 'b']
    histogram_list('a b c a b') == ['a', 'b']
    histogram_list('b b b b a') == ['b']
    histogram_list('') == []

    
	Include these tokens in the code: if test == " ": return {}
	"""
    pass


def histogram_max(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram_max('a b c') == 'a'
    histogram_max('a b b a') == 'b'
    histogram_max('a b c a b') == 'b'
    histogram_max('b b b b a') == 'b'
    histogram_max('') == ''

    
	Include these tokens in the code: if test == " ": return {}
	"""
    pass


def histogram_max_list(test):
    """Given a string representing a space separated lowercase letters, return a list
    of the letters with the most repetition.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram_max_list('a b c') == ['a']
    histogram_max_list('a b b a') == ['b', 'a']
    histogram_max_list('a b c a b') == ['b', 'a']
    histogram_max_list('b b b b a') == ['b']
    histogram_max_list('')