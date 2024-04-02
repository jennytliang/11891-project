def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    return sum(lst[::2])

"""Doc Tests
>>> solution([5, 8, 7, 1])  #  odd_at_even
12
>>> solution([3, 3, 3, 3, 3])  #  all 3s sum to 9
9
>>> solution([30, 13, 24, 321])  #  321 is not in any even position
0 
>>> solution([4, 6, 11, 9, 10, 15]) # 4 + 9 + 15 = 28
32
>>> solution([4, 8, 11, 9, 10, 15]) # 9 sum to 40
24
>>> solution([4, 8, 11, 9, 10, 12]) # 4 + 12
16
"""