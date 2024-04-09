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
	Do not include these tokens in the code: co
	'''
    if lst == []:
        return -1
    count = [0] * (max(lst) + 1)
    for x in lst:
        count[x] += 1
    for x in range(len(count)):
        if count[x] >= x and x != 0:
            return x
    return -1


if __name__ == '__main__':
    print('Example:')
    print(search([4, 1, 2, 2, 3, 1]))
    print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
    print(search([5, 5, 4, 4, 4]))
    print(search([5, 5, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([5, 5, 4, 4]) == -1
    print('Wow, you are doing pretty good. Time to check it!')
