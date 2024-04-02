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
    
	Include these tokens in the code: count
	Do not include these tokens in the code: new _ dict
	'''
    # check if there are any numbers greater than 0
    if len(lst) == 0:
        return -1
    elif lst[0] > 0:
        return lst[0]
    else:
        # count the frequency of each number
        freq = {}
        for num in lst:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # find the number with the highest frequency
        max_freq = 0
        max_num = -1
        for num, freq in freq.items():
            if freq > max_freq:
                max_freq = freq
                max_num = num
        # if a number has a frequency greater than or equal to its value, return the number
        if max_freq >= max_num:
            return max_num
        # otherwise return -1
        else:
            return -1
























































































































































































































































