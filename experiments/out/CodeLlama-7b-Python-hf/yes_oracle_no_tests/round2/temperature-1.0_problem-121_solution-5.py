def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i
	Do not include these tokens in the code: # 1
	"""
    # return sum (lst[num] for num in range (0, len ( lst ) )
    # if ( not ( num % 2 == 0 ) and lst [ num ] % 2 != 0 ))

    total = 0

    for i in lst:
        if i % 2 == 1:
            num = lst.index(i)
            if num % 2 == 0:
                total += i

    return total


# print(solution([5, 8, 7, 1]))  # -> 12
# print(solution([3, 3, 3, 3, 3]))  # -> 9
# print(solution([30, 13, 24, 321]))  # -> 0
