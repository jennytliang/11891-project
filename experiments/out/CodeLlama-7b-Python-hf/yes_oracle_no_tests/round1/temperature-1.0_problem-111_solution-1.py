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
test = "a b c"
hist = histogram(test)
if hist == {'a': 1, 'b': 1, 'c': 1}:
    print("Test passed")
else:
    print("Test failed")

# CASE 2
test = "a b b a"
hist = histogram(test)
if hist == {'a': 2, 'b': 2}:
    print("Test passed")
else:
    print("Test failed")

# CASE 3
test = "a b c a b"
hist = histogram(test)
if hist == {'a': 2, 'b': 2}:
    print("Test passed")
else:
    print("Test failed")

# CASE 4
test = "b b b b a"
hist = histogram(test)
if hist == {'b': 4}:
    print("Test passed")
else:
    print("Test failed")

# CASE 5
test = " "
hist = histogram(test)
if hist == {}:
    print("Test passed")
else:
    print("Test failed")
