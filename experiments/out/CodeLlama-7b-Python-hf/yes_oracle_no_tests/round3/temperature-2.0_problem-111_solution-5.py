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
    # TODO: Write your solution here
    result = {}
    for i in test.split():
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    return result


# TESTS
# Test 1
test = "a b c a b"
expected = {'a': 2, 'b': 2}
print "Test 1. Expected:", expected
actual = histogram(test)
print "Actual:", actual
print "Equal?", expected == actual

# Test 2
test = "a b c"
expected = {'a': 1, 'b': 1, 'c': 1}
print "\nTest 2. Expected:", expected
actual = histogram(test)
print "Actual:", actual
print "Equal?", expected == actual

# Test 3
test = "a b c a b"
expected = {'a': 2, 'b': 2}
print "\nTest 3. Expected:", expected
actual = histogram(test)
print "Actual:", actual
print "Equal?", expected == actual

# Test 4
test = ""
expected = {}
print "\nTest 4. Expected:", expected
actual = histogram(test)
print "Actual:", actual
print "Equal?", expected == actual

# Test 5
test = "a a a a b"
expected = {'a': 4, 'b': 1}
print "\nTest 5. Expected:", expected
actual = histogram(test)
print "Actual:", actual
print "Equal?", expected == actual

# Test 6
test = "a b c a b"
expected = {'a': 2, 'b': 2}
print "\nTest 6. Expected:", expected
actual = histogram(test)
print "Actual:", actual
print "Equal?", expected == actual

# Test 7
test = "a a a a a a a"
expected = {'a': 7}
print "\nTest 7. Expected