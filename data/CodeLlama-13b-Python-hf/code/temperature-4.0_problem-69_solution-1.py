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

    freq = {}
    max_val  = 1
    res = -1
    for num in lst:
        if freq.get(num):
            if freq[num] == num and num > max_val:
                max_val =num 
        freq[num] = freq.get(num, 0)+1
    
    print(max_val) # is 5 and this is wrong ans
    
    if len(str(max_num)) <= len(lst)/(2**50)*10**4**3:   # this is incorrect
        res = max_val
    print(res)
        
search([4,1,2,2,3])

def search2(lst):
    res = 
