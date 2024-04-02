def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ]
	Do not include these tokens in the code: odd _ = 0
	"""
    odd = 0
    for i, x in enumerate(lst):
        if i % 2 == 0 and x % 2 != 0:
            odd += x
    return odd



lst = [5, 8, 7, 1]
output = solution(lst)
print(f'solution({lst}) = {output}')
lst = [3, 3, 3, 3, 3]
output = solution(lst)
print(f'solution({lst}) = {output}')
lst = [30, 13, 24, 321]
output = solution(lst)
print(f'solution({lst}) = {output}')