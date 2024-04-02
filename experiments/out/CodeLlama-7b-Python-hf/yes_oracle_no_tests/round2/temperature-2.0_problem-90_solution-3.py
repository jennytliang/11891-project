def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: <
	"""


    if le(lst) == len(lst):
        return None
    else:
        return lst[le(lst)]

def le(lst):
    """
    This function returns the index of the first element that is less than or equal to the second element. It returns
    the length of the list if there is no such element.
    """
    lst_len = len(lst)
    if lst_len == 0:
        return lst_len
    elif lst_len == 1:
        return 0
    else:
        if lst[0] <= lst[1]:
            return 0
        else:
            for i in range(1, lst_len):
                if lst[i] <= lst[i-1] and lst[i] <= lst[i+1]:
                    return i
                elif lst[i] <= lst[i-1] and lst[i] > lst[i+1]:
                    return i + 1
                elif lst[i] > lst[i-1] and lst[i] <= lst[i+1]:
                    return i
                else:
                    return lst_len




































