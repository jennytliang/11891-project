def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    res = 0
    for num, i in zip(lst, range(len(lst))):
        if not(i % 2) and num % 2:
            res += num

    return res


solution([5, 8, 7, 1])
