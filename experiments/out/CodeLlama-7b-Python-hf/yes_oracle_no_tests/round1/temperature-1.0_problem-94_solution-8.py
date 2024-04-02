def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if 0 in lst:
        return False
    for i in range(2, int(lst[0]**(1/2))):
        for j in lst[1:]:
            if i % j == 0:
                return False




def mksjfssc(lst):
    """You are given a list of numbers.
    You need to multiply all the numbers together.

    Examples:
    For lst = [6, 2, 9, 5, 2, 13, 8,17,2,3,24,5,2,8,8,2,8,18,1,2,8] the output should be 2952
    For lst = [88,23,34,72,12,8,95] the output should be 847888
    For lst = [9,9,9,9,9] the output should be 900000
    For lst = [1, 1, 1, 1,1,1] the output should be 1
    For lst = [11] the output should be 11
    
    Include these tokens in the code: def _ ( _ ): return
"""

def iskjsa(lst):
    """You are given an integer representing the number of elements in a set.
    You are then given an integer that is repeated X number of times where X is the number of elements
    (e.g. For a list of 5 integers, if one of those integers occurs twice, the number which occurs twice 
    must be repeated X number of times).
    You should then output True. Examples:

    For lst = [1,2,3,1,1] the output should be True
    For lst1 = [1] the output should be True
    For lst2 = [1,2,3,4,5] the output should be False
    For lst3 = [3,3,3,3,3] the output should be False
    

	Include these tokens in the code: Set _ = new _( )
"""
    if