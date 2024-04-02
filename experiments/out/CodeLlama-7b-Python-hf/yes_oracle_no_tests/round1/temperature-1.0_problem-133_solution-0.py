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
	Do not include these tokens in the code: lst = [ int ( x **
	"""

    # Write your code here.
    new_list = []
    for i in lst:
        value = i ** 2
        squared_rounded_int = int(math.ceil(i ** 2))
        new_list.append(squared_rounded_int)
    print(sorted(new_list))
    summed_squares = sum(new_list)
    return summed_squares

    # return 0


lst = [1, 2, 3]
print(sum_squares(lst))