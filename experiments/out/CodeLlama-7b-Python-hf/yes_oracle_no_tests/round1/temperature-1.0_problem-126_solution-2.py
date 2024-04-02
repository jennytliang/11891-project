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
    
    
    # check if list has more than one duplicate
    dict = {}
    #count = len(lst)-len(set(lst))
    counts = dict.fromkeys(lst, 0) # {1:0, 2:0, …}
    for n in lst:
        counts[n] += 1 # counts = {5:1, 8:1, 2:1, 9:1…}

    # check if any value in number of duplciates is more than one
    
    for i in counts.values():
        if i > 1:
            return False
            
    
    # now sort list and check if values were swapped
    lst = sorted(lst)
	for idx, n in enumerate(lst):
		if lst[idx]< lst[idx-1]:
			return False




#print(is_sorted([1, 2, 7, 3, 3, 8, 4, 1, 6, 4]))