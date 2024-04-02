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
    
	Include these tokens in the code: is _ prime
	"""

  	# Input the variables a and b in pairs for the intervals
    a_start, a_end = interval1
    b_start, b_end = interval2
    
    # Check if a or b is within a and b (respectively)
    if a_start < b_start < a_end < b_end:
        start = a_end
        end = b_end
    elif a_start < b_start < b_end < a_end:
        start = a_end
        end = b_end
    elif b_start < a_start < a_end < b_end:
        start = a_end
        end = b_end
    elif b_start < a_start < b_end < a_end:
        start = a_end
        end = b_end
    elif a_start < a_end:
        start = max(a_start, b_start)
        end = min(a_end, b_end)
    elif b_start < b_end:
        start = max(a_start, b_start)
        end = min(a_end, b_end)
    else:
        return "NO"
    
    # Check that start is never greater than or less than end to filter out empty set scenarios
    if start < end:
        return "NO"
    
    # Check that the length in integer steps is a prime number by trying to divide the length of the intersection
    if len(range(start, end + 1)) % 2 == 0 or len(range(start, end + 1)) % 3 == 0:
        return "NO"
    return "YES"


#print(intersection((1, 2), (2, 3))) # ==> "NO"
print(intersection((-1, 1), (0, 4))) # ==> "NO"
print(intersection((-3, -1), (-5, 5))) # ==> "YES"
