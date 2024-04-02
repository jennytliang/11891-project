def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    
    total = 0
    for i in range(len(lst)): # for every number in the list
        # check if the number at index i is odd and at an even index
        if (lst[i] % 2 == 1) and ((i+1)%2 == 0):
            total = total + lst[i] # Add to the total
    
    return total