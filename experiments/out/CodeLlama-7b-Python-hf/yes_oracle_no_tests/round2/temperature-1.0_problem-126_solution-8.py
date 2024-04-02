def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    
	Include these tokens in the code: count = dict ()
	Do not include these tokens in the code: def is _ sorted ( lst
	'''
    # my initial solutions
    # a set returns an ordered list of items in another iterable
    # sorted() is ascending order
    # 
    if len(lst) != len(set(lst)):
        pass
        return False
    return bool(lst == sorted(lst))

    if len(lst) != len(set(lst)):
        return False
    else:
        return bool(lst == sorted(lst))


#print(is_sorted([5]))  # expected: True
#print(is_sorted([1, 2, 3, 4, 5]))  # expected: True
#print(is_sorted([1, 3, 2, 4, 5]))  # expected: False
#print(is_sorted([1, 2, 3, 4, 5, 6]))  # expected: True
#print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # expected: True
#print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # expected: False
#print(is_sorted([1, 2, 2, 3, 3, 4]))  # expected: True
#print(is_sorted([1, 2, 2, 2, 3, 4]))  # expected: False

#print(is_sorted([17, 11, 30, 22, 16, 12, 16]))  # expected: False
#print(is_sorted([17, 11, 26, 30, 22, 16, 12,16]))  # expected: False

# SORTED
sortedlst = [1, 2, 2, 3, 3, 4]

sortedlst[0]


sortedlst[1]
sortedlst[-1]= 4
sortedlst

sortedlst.sort()

lst = [1] + lst
lst






from timeit import timeit
times = []
