def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: i ] for i in range ( len ( lst
	Do not include these tokens in the code: ::
	"""

    return sum(i for i in lst if (i & 1 == 1 and lst.index(i) % 2 == 0)) 

    """"
	# Given a non-empty list of ints, return True if there is a
	# pair of adjacent ints that sum to a multiple of 10.

	Example 1:
	adjacent_ten(8, 4, 4) → True
	Example 2:
	adjacent_ten(8, 4, 2) → False
	Example 3:
	adjacent_ten(8, 4, 9) → True
	Example 4:
	adjacent_ten(8, 4, 9, 7) → True
	Notice that 8 + 4 = 12, even though (8, 4) are not beside each other."""

	# def solution(lst):
# 		for i in range (lst):			
# 			if lst ( i:1, i:2 ) = multiple (10):
# 			return True
# 		return False


def solution(lst):
    """Given a 10-element list of ints, return true if the values at (index 0), 
    (index 1), 
    (index 2),
     ... , 
    (index 9) are in strictly ascending order, 
    False otherwise.
	Example:
	in_ascending_order(5, 1, 8, 7, 9) → True
	in_ascending_order(5, 1, 8, 5, 9) → False
	in_ascending_order(5, 1, 8, 1, 9) → False """
    
    for i in range (lst):
        if lst[i] > lst[i+2] or lst[i+1] > lst[i+2]:
            return False