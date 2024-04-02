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

    # In this first function that a person writes when learning 
    # algorithms, we have a problem with a specific use case 
    # (testing the code) that we should fix.
    # Some people have done a quick and dirty fix because 
    # they thought the problem was a minor one. It makes sense to 
    # check if the result is a prime number, but it really should 
    # be checked that the result of the intersection of two 
    # interval(s) is a prime number. This is not the code to fix,
    # that should be done in another function.
    
    # This is not the code to fix, that should be done in another 
    # function.
    
    ##############################################################
    lowerRange1 = min(interval1)
    lowerRange2 = min(interval2)
    upperRange1 = max(interval1)
    upperRange2 = max(interval2)
    ##############################################################
    # We have to check that two intervals intersect
    if (lowerRange1 == lowerRange2 == upperRange1 == upperRange2):
        return "NO"

    # In case they do not intersect...
    elif (lowerRange1 > upperRange2 or upperRange1 < lowerRange2):
        return "NO"

    # We have to consider the 4 cases...
    elif (lowerRange1 <= lowerRange2 <= upperRange1 <= upperRange2):
        return intersection_1([lowerRange1, lowerRange2], [upperRange1, upperRange2])
    
    elif (lowerRange2 <= lowerRange1 <= upperRange2 <= upperRange1):
        return intersection_1([lowerRange1, lowerRange2], [upperRange1, upperRange2])

    elif (lowerRange1 <= lowerRange2 <= upperRange2 <= upperRange1):
        return intersection_1([lowerRange1, lowerRange2], [upperRange1, upperRange2])

    elif (lowerRange2 <= lowerRange1 <= upperRange1 <= upperRange2):
        return intersection_1([lowerRange1, lowerRange2], [upperRange1, upperRange2])

def intersection_1(interval1