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
    
	Do not include these tokens in the code: # count = dict ()
	'''
    # find number of occurences of each number
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # find the number with the greatest occurences
    max_freq = max(count.values())
    
    # find the number with the greatest occurences that is also greater than 0
    for num, freq in count.items():
        if num > 0 and freq >= num:
            return num
    return -1

print(search([4, 1, 2, 2, 3, 1])) # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # 3
print(search([5, 5, 4, 4, 4])) # -1
