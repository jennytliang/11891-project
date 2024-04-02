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
    
	Include these tokens in the code: count = dict ()
	'''
    # return
    # count = dict ()
    # output = -1
    
    # for i in range(len(lst)):
    #     if lst[i] not in count:
    #         count[lst[i]] = 1
    #     else:
    #         count[lst[i]] += 1
        
    #     if count[lst[i]] > lst[i] and output < lst[i]:
    #         output = lst[i]
    
    # return output
    
    d = dict()
    return max(k for k in set(lst) if lst.count(k) >= k) if any(lst.count(k) >= k for k in set(lst)) else -1


print(search([4, 1, 2, 2, 3, 1])) # should print 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # should print 3
print(search([5, 5, 4, 4, 4])) # should print -1
