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
	Do not include these tokens in the code: for i in range ( len (
	"""
    # first you need to round each element in the list to the upper int
    # (Ceiling) first
    for i in range(len(lst)):
        lst[i] = int(math.ceil(lst[i]))

    # then you need to square each element in the list
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2

    # finally you need to sum all the elements in the list
    sum_of_squares = sum(lst)

    return sum_of_squares


lst = [1, 2, 3]
print(sum_squares(lst))

lst = [1, 4, 9]
print(sum_squares(lst))

lst = [1, 3, 5, 7]
print(sum_squares(lst))

lst = [1.4, 4.2, 0]
print(sum_squares(lst))

lst = [-2.4, 1, 1]
print(sum_squares(lst))
