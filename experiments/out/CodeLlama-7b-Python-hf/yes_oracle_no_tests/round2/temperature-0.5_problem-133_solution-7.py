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
	Do not include these tokens in the code: new _ lst = []
	"""
    sum_squares = 0
    for num in lst:
        num = int(math.ceil(num))
        sum_squares += num ** 2
    return sum_squares


#print(sum_squares([1,2,3]))
#print(sum_squares([1,4,9]))
#print(sum_squares([1,3,5,7]))
#print(sum_squares([1.4,4.2,0]))
#print(sum_squares([-2.4,1,1]))

#or 

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
	Do not include these tokens in the code: new _ lst = []
	"""
    sum_squares = 0
    for num in lst:
        num = int(math.ceil(num))
        sum_squares += num ** 2
    return sum_squares


lst = [1,2,3]
print(sum_squares(lst))
lst = [1,4,9]
print(sum_squares(lst))
lst = [1,3,5,7]
print(sum_squares(lst))
lst = [1.4,4.2,0]
print(sum_squares(lst))
lst = [-2.4,1,1]
print(sum_squares(lst))