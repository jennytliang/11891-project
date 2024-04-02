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
    # count = dict ()
    # for i in lst:
    #     if i in count:
    #         count[i] += 1
    #     else:
    #         count[i] = 1

    # for i in lst:
    #     if count[i] > i:
    #         return i

    # return -1

    # count = dict()
    # for i in lst:
    #     if i in count:
    #         count[i] += 1
    #     else:
    #         count[i] = 1
    # max_freq = 0
    # for i in count:
    #     if count[i] >= i and count[i] > max_freq:
    #         max_freq = count[i]
    # return max_freq

    count = dict()
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return max(i for i in count if count[i] >= i and count[i] > i) if count else -1


if __name__ == '__main__':
    lst = [4, 1, 2, 2, 3, 1]
    print(search(lst))
