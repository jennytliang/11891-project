def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    evens = lst[::2]
    odds = lst[1::2]
    odds_in_evens = [x for x in evens if x % 2 == 1]
    return sum(odds_in_evens)


def solution2(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    return sum(i for i in range(0, len(lst), 2) if lst[i] % 2 != 0)


# print(solution([5, 8, 7, 1]))
# print(solution([3, 3, 3, 3, 3]))
# print(solution([30, 13, 24, 321]))

print(solution2([5, 8, 7, 1]))
print(solution2([3, 3, 3, 3, 3]))
print(solution2([30, 13, 24, 321]))
