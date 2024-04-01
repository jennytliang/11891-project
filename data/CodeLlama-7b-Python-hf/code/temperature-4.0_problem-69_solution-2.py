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
    if not lst[-1] > 0:
        return -1

    for el in lst[-1::-1]:
        if el > 0 and lst[0] != el:
            if lst.count(el) <= el:
                return -1
            else:
                return el
                
print(f"search([4, 0, 2, 2, 3, 1]) returns {search([4, 0, 2, 2, 3, 1])}")       