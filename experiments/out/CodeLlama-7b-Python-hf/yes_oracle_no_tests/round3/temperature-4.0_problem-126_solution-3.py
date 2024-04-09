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
    
	Include these tokens in the code: not
	'''


    count = dict()
  
    for x in lst:
   
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    for key in count.keys():
        if count[key] > 1:
            return False
    
    return sorted(lst) == lst


is_sorted([5]) #➞ True
#is_sorted([1, 2, 3, 4, 5]) #➞ True
#is_sorted([1, 3, 2, 4, 5]) #➞ False
#is_sorted([1, 2, 3, 4, 5, 6]) #➞ True
#is_sorted([1, 2, 3, 4, 5, 6, 7]) #➞ True
#is_sorted([1, 3, 2, 4, 5, 6, 7]) #➞ False
#is_sorted([1, 2, 2, 3, 3, 4]) #➞ True
#is_sorted([1, 2, 2, 2, 3, 4]) #➞ False

