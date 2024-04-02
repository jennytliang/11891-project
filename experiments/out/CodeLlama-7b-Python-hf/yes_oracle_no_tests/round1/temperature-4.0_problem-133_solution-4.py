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
    

    
	Include these tokens in the code: import math
	"""
    #print(lst)
    lst2 = []
    for i in lst:
        if i < 0:
            lst2.append(i)
        else:
            lst2.append(math.ceil(i))
    print(lst2)
    sum = 0
    for i in lst2:
        sum = sum + (i ** 2)
    return sum


lst = []
lst = [int(i) for i in input().split()]
print(sum_squares(lst))
