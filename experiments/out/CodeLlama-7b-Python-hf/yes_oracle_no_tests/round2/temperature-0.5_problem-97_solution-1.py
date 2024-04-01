def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int ( str ( a )[ - 1 ])
	"""
    return int(str(a)[-1]) * int(str(b)[-1])

# RW 04/08/2020
# This is a good example of a problem that could be solved using 
# string slicing.  The instructions ask for the unit digit of the 
# product, which is the same as the unit digit of the product of the 
# unit digits.  This is a very simple problem, and I'm sure there 
# are many ways to solve it.  However, I'm going to solve this one 
# way, using string slicing.  I'm going to assume that the input is 
# always valid.

# The input is always valid, so that means that the input is a 
# positive integer.  Since we're only interested in the unit digit, 
# we can just convert the integer to a string and use string slicing 
# to get the last character.  We can then convert that character to 
# an integer and return it.  I'm going to use the format of the 
# problem statement to show you how to do this.

# The format of the problem statement says to do this:
# return int ( str ( a )[ - 1 ])

# Note that the string slicing operation is [ - 1 ], not [ -1 ].  I 
#'m not sure why the space is there, but I'm going to assume that's 
# how it's supposed to be.  The reason for using [ - 1 ] is that 
# the string slicing operation is [ start : end : step ].  The 
# start is the index of the first character to include, the end is 
# the index of the first character to exclude, and the step is the 
# increment between characters.  Since we want the last character, 
# we need to use -1 for the end, but we don't want to count the 
# last character, so we use -1 for the step.  Since we want the 
# last character, the start is the length of the string minus 1, 
# so we use -1 for the start