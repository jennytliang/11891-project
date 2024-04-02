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
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	'''


    def largest_smallest_integers(lst):
        result = []
        for i in lst:
            if i < 0:
                result.append(i)
        result = list(set(result))
        result.sort()
        if len(result) == 0:
            return (None, None)
        else:
            return (result[-1], result[0])

    return largest_smallest_integers(lst)


# TESTS

# Test 1
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
# expected output: (None, 1)

# Test 2
print(largest_smallest_integers([]))
# expected output: (None, None)

# Test 3
print(largest_smallest_integers([0]))
# expected output: (None, None)
