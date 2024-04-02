def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    total = 0
    lst.sort()
    
    for i in range(0, len(lst), 2):
        if i % 2 != 0:
            continue
        if (lst[i] % 2 == 1):
            total += lst[i]
            
    return total

if __name__ == '__main__':
    print(solution([5, 8, 7, 1]))
    print(solution([5, 8, 6, 1]))
    print(solution([5, 8, 0, 1]))
    print(solution([5, 8, 9, 12]))