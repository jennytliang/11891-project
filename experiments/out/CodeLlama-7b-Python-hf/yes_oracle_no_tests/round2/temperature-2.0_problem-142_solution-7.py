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
    # if len(lst) == 0:
    #     return 0
    # else:
    #     lst[0] = lst[0] ** 2
    #     return sum_squares(lst[1:]) + lst[0]

    # if len(lst) == 0:
    #     return 0
    # else:
    #     lst[0] = lst[0] ** 2 if lst[0] % 3 == 0 else lst[0]
    #     lst[0] = lst[0] ** 3 if lst[0] % 4 == 0 else lst[0]
    #     return sum_squares(lst[1:]) + lst[0]

    if len(lst) == 0:
        return 0
    else:
        lst[0] = lst[0] ** 2 if lst[0] % 3 == 0 else lst[0]
        lst[0] = lst[0] ** 3 if lst[0] % 4 == 0 else lst[0]
        return sum_squares(lst[1:]) + lst[0]


def main():
    print(sum_squares([1, 2, 3]))
    print(sum_squares([]))
    print(sum_squares([-1, -5, 2, -1, -5]))


if __name__ == "__main__":
    main()
