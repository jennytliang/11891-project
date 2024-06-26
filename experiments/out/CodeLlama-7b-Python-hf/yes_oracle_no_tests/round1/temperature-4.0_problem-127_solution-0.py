def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if interval1[0] <= interval2[0] and interval2[0] <= interval1[1]:
        start = interval2[0]
    elif interval1[0] <= interval2[0] and interval2[0] <= interval1[1]:
        start = interval1[0]
    else:
        return "NO"

    if interval1[0] <= interval2[1] and interval2[1] <= interval1[1]:
        end = interval2[1]
    elif interval1[0] <= interval2[1] and interval2[1] <= interval1[1]:
        end = interval1[1]
    else:
        return "NO"

    length = end - start + 1
    if length == 1 or length == 2:
        return "NO"
    if length == 3:
        return "YES"
    for i in range(2, length):
        if length % i == 0:
            return "NO"
    return "YES"


print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
