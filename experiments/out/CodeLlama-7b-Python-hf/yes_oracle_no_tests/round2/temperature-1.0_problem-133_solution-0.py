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
	Do not include these tokens in the code: # Write your code here .
	"""
    s = 0
    lst_up = []
    
    # round each element to the upper value
    for i in lst:
        lst_up.append( math.ceil(i) )
    # print("\n Rounded : ", lst_up, "\n")
        
    # calculate the sum of squared numbers in the given list
    for i in lst_up:
        s = s + pow(i,2)
    
    return int(s)

