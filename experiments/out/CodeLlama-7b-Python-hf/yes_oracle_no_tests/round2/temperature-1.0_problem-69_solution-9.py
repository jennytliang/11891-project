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
	Do not include these tokens in the code: if lst == [] : return -
	'''
    lst2 = [lst.count(i) for i in lst if i > 0]
    lst2 = [i for i in lst2 if i >= i]
    if lst2:
        lst2 = [i for i in lst2 if i for i == i]
        if lst2:
            return max(lst2)
    return -1

if __name__ == '__main__':
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([1, 2, 2]) == -1

    print("Great! It seems like your code is working perfectly. :)")
