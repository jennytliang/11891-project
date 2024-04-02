def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    
	Do not include these tokens in the code: This function will take a list of
	"""
    if lst == []:
        return 0

    sum_of_squares = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum_of_squares += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            sum_of_squares += lst[i]**3
        else:
            sum_of_squares += lst[i]
    return sum_of_squares


def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([1, 2, 3, 4, 5]) == 33
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 106
    assert sum_squares([1, 2, 3, 4, 5, 6, 7]) == 236
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 386
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 606
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 846
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 1086
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1326
