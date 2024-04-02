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
        if a == 1:
            return False
        elif a == 2:
            return True
        elif a % 2 == 0:
            return False

        counter = 3
        limit = int(a ** 0.5)
        while counter <= limit:
            if a % counter == 0:
                return False
            counter += 2

        return True


    def intersection(interval1, interval2):
        intersect = False
        intersection = []

        if interval2[0] <= interval1[0] and interval1[1] <= interval2[1]:
            if is_prime(interval1[1] - interval1[0] + 1):
                intersect = 'YES'
            else:
                intersect = 'NO'

        elif interval1[0] <= interval2[0] and interval2[1] <= interval1[1]:
            if is_prime(interval2[1] - interval2[0] + 1):
                intersect = 'YES'
            else:
                intersect = 'NO'
        
        elif interval2[0] < interval1[0] < interval2[1] < interval1[1]:
            intersect = 'NO'

        elif interval1[0] < interval2[0] < interval1[1] < interval2[1]:
            intersect = 'NO'

        elif interval1[0] <= interval2[0] and interval2[0] < interval1[1] <= interval2[1]:
            if is_prime(interval1[1] - interval2[0] + 1):
                intersect = 'YES'

            else:
                intersect = 'NO'
        
        elif interval2[0] <= interval1[0] and interval1[0] < interval2[1] <= interval1[1]:
            if is_prime(interval2[1] - interval1[0] + 1):
                intersect = 'YES'

            else:
                intersect = 'NO'

        return intersect

################################################################################


################################################################################
################################################################################