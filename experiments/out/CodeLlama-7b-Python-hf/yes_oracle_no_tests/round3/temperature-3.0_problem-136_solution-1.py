def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    
	Include these tokens in the code: ))
	Do not include these tokens in the code: )
	'''


    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    if neg == []:
        neg = None
    if pos == []:
        pos = None

    return (max(neg), min(pos))


# TESTS
# --------------------------------------------------------------------
# Test 1
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
# (None, 1)

# Test 2
print(largest_smallest_integers([]))
# (None, None)

# Test 3
print(largest_smallest_integers([0]))
# (None, None)

# Test 4
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7]))
# (-7, -1)

# Test 5
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0]))
# (-7, -1)

# Test 6
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0, 1]))
# (-7, -1)

# Test 7
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0, 1, 2]))
# (-7, -1)

# Test 8
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0, 1, 2, 3]))
# (-7, -1)

# Test 9
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0, 1, 2, 3, 4]))
# (-7, -1)

# Test 10
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0