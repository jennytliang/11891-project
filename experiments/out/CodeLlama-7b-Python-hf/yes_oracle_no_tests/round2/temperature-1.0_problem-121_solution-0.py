def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ] for i in
	"""
    sum = 0

    for i in lst:

        if i % 2 != 0:
            continue
        if lst.index(i) % 2 == 0:
            sum  = sum + i
    return sum
           
assert (solution([5, 8, 7, 1]) == 12), "First error"
assert (solution([3, 3, 3, 3, 3]) == 9), "Second error"
assert (solution([30, 13, 24, 321]) == 0), "Third error"
assert (solution([5, 9, 11]) == 15), "Fourth error"
