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
    # Input: Intervals: Tuples of two integers
    # Output: 'YES' or 'NO'
    # Assumptions: The first interval is always the smaller one
    # Intervals are closed, so they include both start and end
    # Intervals are sorted (smaller first)
    # Intervals have positive values, but not necessarily

    # Solution 1
    # Check if the intervals intersect first
    # If they do, generate a list of numbers between the two intervals
    # Check if any of those numbers are prime
    # If they are, return 'YES'
    # If they are not, return 'NO'
    # If they don't intersect, return 'NO'

    # Solution 2
    # Check if the intervals intersect first
    # If they do,
    # Check if the length of the intersection is prime
    # If it is, return 'YES'
    # If it is not, return 'NO'
    # If they don't intersect, return 'NO'

    # Solution 3
    # Check if the intervals intersect first
    # If they do,
    # Calculate the length of the intersection
    # Check if the length of the intersection is prime
    # If it is, return 'YES'
    # If it is not, return 'NO'
    # If they don't intersect, return 'NO'

    # Solution 4
    # Check if the intervals intersect first
    # If they do,
    # Calculate the length of the intersection
    # If the length of the intersection is prime, return 'YES'
    # If it is not, return 'NO'
    # If they don't intersect, return 'NO'


    def is_prime(a):
        if a == 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        if interval1[0] <= interval2[0] <= interval1[1]:
            if interval2[0] <= interval1[1] <= interval2[1]:
                length = interval