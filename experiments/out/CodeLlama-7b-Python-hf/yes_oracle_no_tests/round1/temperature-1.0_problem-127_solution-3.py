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

    def is_prime(a):
        if len(set(a))==a:
            a = range(1, a+1, 2)
            return all(a%i>0 for i in a)
        return False

    start1, end1 = interval1
    start2, end2 = interval2

    if start2>start1:
        interval1, interval2 = interval2, interval1

    intersection = list(range(min(start2, end1), max(start2, end1)+1))
    if len(intersection)<2:
        return "NO"
    else:
        a = len(intersection)
        if a>0 and is_prime (a):
            return "YES"
        else:
            return "NO"


    """
    import math
    
    length = 0
    
    if(interval1[0] == interval2[1] and interval2[0] == interval1[1]):
        length = interval2[1] - interval2[0]
        
    return "YES" if 
    """