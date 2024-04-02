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
    # write your code here
    # return sum_squares([1,2,3])
    # return sum_squares([])
    # return sum_squares([-1,-5,2,-1,-5])

    # print(lst)
    # print(lst[0])
    # print(lst[1])
    # print(lst[2])
    # print(lst[3])
    # print(lst[4])

    result = 0
    for index in range(len(lst)):
        if index % 3 == 0:
            result += lst[index] ** 2
        elif index % 4 == 0 and index % 3 != 0:
            result += lst[index] ** 3
        else:
            result += lst[index]
    return result


def sum_squares(lst):
    result = 0
    for index in range(len(lst)):
        if index % 3 == 0:
            result += lst[index] ** 2
        elif index % 4 == 0 and index % 3 != 0:
            result += lst[index] ** 3
        else:
            result += lst[index]
    return result


print(sum_squares([1, 2, 3]))
print(sum_squares([]))
print(sum_squares([-1, -5, 2, -1, -5]))
