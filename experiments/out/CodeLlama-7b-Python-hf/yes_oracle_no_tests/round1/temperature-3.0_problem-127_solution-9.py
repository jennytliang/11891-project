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
    # Input: a tuple of two tuples of integers
    # Output: a string, "YES" or "NO"
    
    # 1st solution:
    # O(n) time | O(1) space
    def is_prime(a):
        if a == 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    def intersection(interval1, interval2):
        # if the intervals don't intersect, return "NO"
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return "NO"
        
        # if they intersect, find the smaller interval and check if the length of intersection
        # is a prime number
        if abs(interval1[0] - interval2[0]) < abs(interval1[1] - interval2[0]):
            smaller_interval = interval2
            bigger_interval = interval1
        else:
            smaller_interval = interval1
            bigger_interval = interval2
        intersection_length = bigger_interval[1] - smaller_interval[0] + 1
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"
    
    # 2nd solution:
    # O(n) time | O(1) space
    def intersection(interval1, interval2):
        # if the intervals don't intersect, return "NO"
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return "NO"
        
        # if they intersect, find the smaller interval and check if the length of intersection
        # is a prime number
        smaller_interval = interval1 if abs(interval1[0] - interval2[0]) < abs(interval1[1] - interval2[0]) else interval2
        bigger_interval = interval2 if smaller_interval is interval1 else interval1
        intersection_length = bigger_interval[1] - smaller_interval[0] + 1
        if is_prime(intersection