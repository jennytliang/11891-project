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

    nega = []
    posi = []
    for i in lst:
        if i < 0:
            nega.append(i)
        elif i > 0:
            posi.append(i)
    if nega == []:
        nega = None
    if posi == []:
        posi = None
    return (max(nega), min(posi))

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([0, 0, 0, 0]))
print(largest_smallest_integers([2, 4, 1, 3, -5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7]))
