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
    
	Include these tokens in the code: lambda
	Do not include these tokens in the code: lam da
	'''


    neg = list(f for f in lst if f < 0)
    pos = list(f for f in lst if f >= 0)

    if pos == []:
        return None, None
    else:
        return max(neg), min(pos)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([0, -1]))
print(largest_smallest_integers([0, -1, -2, -3, -4, -5, -6, -7]))
print(largest_smallest_integers([0, 1, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, 1, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, 0, 1, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, 0, 1, 2, 3, 4, 5, 6, 7, -2, -3, -4, -5, -6, -7]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7