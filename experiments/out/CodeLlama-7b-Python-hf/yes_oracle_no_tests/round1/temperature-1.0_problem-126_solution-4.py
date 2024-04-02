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
	'''
    is_sorted = True
    list_uniquevalues = []
    count = 0
    
    for x in lst:
        if x in list_uniquevalues:
            print(x, 'is a duplicate')
            is_sorted = False
        else:
            list_uniquevalues.append(x) 
            
    list_uniquevalues = sorted(list_uniquevalues)

    # Sort the list.
    for i, x in enumerate(lst):
        if list_uniquevalues[i] != lst[i]:
            is_sorted = False

    if (is_sorted):
        print("List of:", lst, "is_sorted:", is_sorted)
    else:
        print("List of:", lst, "is_sorted:", is_sorted)


answer = is_sorted([1, 2, 2, 2])
answer = is_sorted([1, 2, 3, 9])
answer = is_sorted([1, 2, 3, 5, 9])
answer = is_sorted([5,5])
answer = is_sorted([-1, 1, 2, 3, 4, 5])
answer = is_sorted([9, 5, 6, 2, 8, 40, 12, 13, 5, 1, -2, 1, 15, 17, 2])