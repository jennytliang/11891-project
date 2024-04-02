def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    return sum([lst[i] for i in range(len(lst)) if not (i % 2) and lst[i] % 2])


# OTHER SOLUTIONS

def solution(lst):
    return sum([lst[i] for i in range(len(lst)) if not (i % 2) and lst[i] % 2])


def solution(lst):
    return sum([v for i, v in enumerate(lst) if i % 2 == 0 and v % 2 != 0])


def solution(lst):
    return sum(v for i, v in enumerate(lst) if i % 2 == 0 and v % 2 != 0)


def solution(lst):
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)


def solution(lst):
    return sum(lst[i] for i in range(0, len(lst), 2) if not (lst[i] % 2))
