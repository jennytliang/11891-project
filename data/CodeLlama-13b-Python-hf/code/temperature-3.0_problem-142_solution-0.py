def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    
    sum1 = 0
    
    for i in range(0, len(lst)):
        if i%3 == 0:
            lst[i] = lst[i]**2
            sum1 += lst[i]
        if i%4 == 0:
            if i%3 != 0:
                lst[i] = lst[i]**3
                sum1 += lst[i]
    
    return sum1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sum_squares([]) == 0, "1st example"
    assert sum_squares([1]) == 1, "2nd example"
    assert sum_squares([1, 2, 3]) == 14, "3rd example"