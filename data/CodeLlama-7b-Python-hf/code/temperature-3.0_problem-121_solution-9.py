def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum = 0
    for idx, elem in enumerate(lst):
        if idx % 2 == 0 and elem %2 != 0:
            sum += elem
    return sum