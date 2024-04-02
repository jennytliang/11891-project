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
    
	Do not include these tokens in the code: # 1 . Create a list
	'''
    # 2 . Return largest negative integer, smallest positive integer, or None
    pass


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0, 1]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0, 1, 2]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0, 1, 2, 3]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0, 1, 2, 3, 4]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0, 1, 2, 3, 4, 10]))
print(largest_smallest_integers([2, 4, 1, 3, 5, -7, -12, -1, 0, 1, 2, 3, 4, 10, 11]))
print(largest_smallest_integers([2