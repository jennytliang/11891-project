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
    
	Do not include these tokens in the code: # Tra verse through the list
	'''



    count = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            count += 1
            if count >= lst[i]:
                return lst[i]
    return -1


lst = [4, 1, 2, 2, 3, 1]
print(search(lst))
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4]
print(search(lst))
lst = [5, 5, 4, 4, 4]
print(search(lst))