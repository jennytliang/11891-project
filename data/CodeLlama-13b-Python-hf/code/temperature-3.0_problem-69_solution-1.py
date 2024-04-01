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
    '''
    
    cache = {}
    for i in lst:
        if i not in cache:
            cache[i] = lst.count(i)
    
    return max([x for x in cache if x < cache[x]], default=-1)



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert search([4, 1, 2, 2, 3, 1]) == 2, "First"
