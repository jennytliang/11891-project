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


# TESTS
# CASE 1
print(histogram('a b c'))
# {'a': 1, 'b': 1, 'c': 1}

# CASE 2
print(histogram('a b b a'))
# {'a': 2, 'b': 2}

# CASE 3
print(histogram('a b c a b'))
# {'a': 2, 'b': 2}

# CASE 4
print(histogram('b b b b a'))
# {'b': 4}

# CASE 5
print(histogram(''))
# {}

# CASE 6
print(histogram('a b c a b c a b a'))
# {'a': 3, 'b': 2, 'c': 2}

# CASE 7
print(histogram('a a a a a b b b b b b c c c c d d d d d'))
# {'a': 5, 'b': 4, 'c': 4, 'd': 5}

# CASE 8
print(histogram('a a a a a b b b b b b c c c c d d d d d d'))
# {'a': 5, 'b': 4, 'c': 4, 'd': 5}

# CASE 9
print(histogram('a a a a a b b b b b b c c c c d d d d d d d'))
# {'a': 5, 'b': 4, 'c': 4, 'd': 5}

# CASE 10
print(histogram('a a a a a b b b b b b c c c c d d d d d d d d'))
# {'a': 5, 'b': 4, 'c': 4, 'd': 5}

# CASE 11
print(histogram('a a a a a b b b b b b c c c c d d d d d d d d d'))
# {'a': 5, 'b': 4, 'c':