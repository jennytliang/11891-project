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
    # Input interval1 and interval2 as tuples
    # Return "YES" if the intersection length is prime, "NO" otherwise

    # Check if the two intervals are intersecting
    # If they are not intersecting, return "NO"
    # If they are intersecting, check if the intersection length is prime
    # If the length is prime, return "YES", otherwise return "NO"

    # Your code goes here
    if interval1[0] <= interval2[0] <= interval1[1] or interval2[0] <= interval1[0] <= interval2[1]:
        # Intervals intersect
        # Check if intersection length is prime
        # Get intersection start and end
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        length = end - start + 1

        # Check if length is prime
        if length <= 1:
            return "NO"
        
        # Check if length is prime
        if length == 2:
            return "YES"
        elif length == 3:
            return "YES"
        elif length % 2 == 0 or length % 3 == 0:
            return "NO"
        else:
            return "YES"
    else:
        return "NO"


print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
