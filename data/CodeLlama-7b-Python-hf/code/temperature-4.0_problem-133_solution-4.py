def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    upper_sq = []
    for elm in lst:
        upper_sq.append(abs(int(elm)))

    print(upper_sq)
    if type(lst[0]) != int:
        #print(list(map(int)))

    return(sum(upper_sq)[2:])


my_lst2 = [1, 3, 4, 5, 6, 8,8,88]