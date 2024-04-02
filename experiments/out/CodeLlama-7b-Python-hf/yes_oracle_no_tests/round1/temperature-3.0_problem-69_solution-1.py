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
    # count = {x:lst.count(x) for x in set(lst)}
    # print(count)
    # for k in lst:
    #     if k in count and lst.count(k) >= k:
    #         return k
    # return -1
    return max((k for k in lst if lst.count(k) >= k), default=-1)

# print(search([4, 1, 2, 2, 3, 1]))
# print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
# print(search([5, 5, 4, 4, 4]))
# print(search([1, 2, 3, 4, 5, 6]))


def search_v2(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater 
    than 0, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: count
	Do not include these tokens in the code: new _ dict
	'''
    count = {x:lst.count(x) for x in set(lst)}
    # print(count)
    for k in lst:
        if k in count and lst.count(k) >= k:
            return k
    return -1

print(search_v2([4, 1, 2, 2, 3, 1]))
print(search_v2([1, 2, 2, 3, 3, 3,