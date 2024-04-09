def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # Your code here
	"""
    even_pos_odds = [lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0]
    return sum(even_pos_odds)

# Test cases
print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([5, 8, 7, 1, 12, 9]))

# My own solution
# def solution(lst):
#     return sum([lst[i] for i in range(len(lst)) if i % 2 != 0 and lst[i] % 2 != 0])

# Another solution
# def solution(lst):
#     return sum(lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0)