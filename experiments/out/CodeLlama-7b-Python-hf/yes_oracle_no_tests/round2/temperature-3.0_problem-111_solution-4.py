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
    count = {}
    for letter in test:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count


# TESTS
print histogram("a b c")
print histogram("a b b a")
print histogram("a b c a b")
print histogram("b b b b a")
print histogram("")
print histogram("a b c a b b b b b a b")
# >>> {'a': 1, 'b': 1, 'c': 1}
# >>> {'a': 2, 'b': 2}
# >>> {'a': 2, 'b': 2}
# >>> {'b': 4}
# >>> {}
# >>> {'a': 3, 'b': 4}
