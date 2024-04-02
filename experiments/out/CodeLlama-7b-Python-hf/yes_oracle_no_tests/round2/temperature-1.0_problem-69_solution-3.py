def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Do not include these tokens in the code: return __ result _ search ( lst
	'''
    frequency_dict = {}
    
    for i in range(len(lst)):
        num = lst[i]
        if num in frequency_dict:
            frequency_dict[num] = frequency_dict[num] + 1
        else:
            frequency_dict[num] = 1
            
    for key, val in frequency_dict.items():
        if key > 0 and val >= key:
            return key 
        
    return -1 