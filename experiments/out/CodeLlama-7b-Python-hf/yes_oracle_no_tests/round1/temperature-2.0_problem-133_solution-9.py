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
    # #This is the solution I came up with.
	# #I decided to use a list comprehension to square the numbers, and then round them up.
	# #Then I just summed the list.
    lst = [round(x**2) for x in lst]
    return sum(lst)
    
    # #This is the solution I was given.
    # #It is much more elegant, and uses a built-in function to round.
    # return sum([math.ceil(x**2) for x in lst])
