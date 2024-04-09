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
    if interval1[0] <= interval2[0] <= interval1[1] or interval1[0] <= interval2[1] <= interval1[1]:
        if interval2[0] <= interval1[0] <= interval2[1] or interval2[0] <= interval1[1] <= interval2[1]:
            if interval1[0] >= interval2[0]:
                intersection = (interval1[0], interval2[1])
            elif interval1[0] <= interval2[0]:
                intersection = (interval2[0], interval1[1])
            if intersection[0] > intersection[1]:
                return "NO"
            else:
                if is_prime(intersection[1] - intersection[0] + 1):
                    return "YES"
                else:
                    return "NO"
        else:
            return "NO"
    else:
        return "NO"


def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        for i in range(11, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
