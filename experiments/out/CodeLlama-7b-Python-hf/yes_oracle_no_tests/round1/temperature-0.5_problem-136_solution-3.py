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
    
	Do not include these tokens in the code: atives
	'''

    nega = None
    posi = None

    for i in lst:
        if type(i) == int:
            if i < 0:
                if nega == None or i > nega:
                    nega = i
            elif i > 0:
                if posi == None or i < posi:
                    posi = i

    return (nega, posi)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 0]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6, 0]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6, 0, 1]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6, 0, 1, 2]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6, 0, 1, 2, 3]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6, 0, 1, 2, 3, 4]))
print(largest_smallest_integers([-1, -3, -2, -4, -5, -6, 0, 1, 2, 3, 4, 5]))
print(largest_smallest_integers([-1,