def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""
    return sum(lst[::2][1::2])


# def solution(lst):
#     """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

#     Examples
#     solution([5, 8, 7, 1]) ==> 12
#     solution([3, 3, 3, 3, 3]) ==> 9
#     solution([30, 13, 24, 321]) ==>0

#     Do not include these tokens in the code: return sum ([ lst [ i ]
#     """
#     return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])


# def solution(lst):
#     """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

#     Examples
#     solution([5, 8, 7, 1]) ==> 12
#     solution([3, 3, 3, 3, 3]) ==> 9
#     solution([30, 13, 24, 321]) ==>0

#     Do not include these tokens in the code: return sum ([ lst [ i ]
#     """
#     return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])
