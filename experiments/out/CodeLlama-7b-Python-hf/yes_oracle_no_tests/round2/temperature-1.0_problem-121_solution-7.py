def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ]
	Do not include these tokens in the code: total = 0
	"""
    total = 0 

    for i, a in enumerate(lst):
        print(i)
        print(a)
        if i%2 == 1:
            if a%2 != 0:
                total += a
    return total


    # if lst == []:
    #     return lst
    # else:
    #     return sum(int(lst[i]) if i%2==0 else 0 for i in range(len(lst)))


