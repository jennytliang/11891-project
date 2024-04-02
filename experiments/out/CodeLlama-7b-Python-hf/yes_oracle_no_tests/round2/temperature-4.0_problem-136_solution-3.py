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
    
	Include these tokens in the code: = list
	'''

   # YOUR CODE HERE
    nega = []
    posi = []
    for i in lst:
        if i < 0:
            nega.append(i)
        if i > 0:
            posi.append(i)

    if len(nega) == 0:
        nega = None
    else:
        nega = min(nega)
    if len(posi) == 0:
        posi = None
    else:
        posi = max(posi)
    return (nega, posi)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([0, 0, 0, 0, 0, 0, 0]))
print(largest_smallest_integers([10, 12, 15, -1, -10, -15, -12]))
print(largest_smallest_integers([-9, -10, -11, -12, -13, -14, -15]))
print(largest_smallest_integers([-1, -1, -1, -1, -1, -1, -1]))
print(largest_smallest_integers([-9, -10, -11, -12, -13, -14, -15]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([0, 2, 3, 4, 5, 6, 7]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 0]))
print(largest_smallest_integers([1, 2, 3, 4, 5, 6]))
print(largest_smallest_integers([]))
