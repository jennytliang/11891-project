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
    def is_prime(n):
        """
        Input:
        - n: a number
        Output:
        - boolean: whether n is a prime number
        """
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    if interval1[0] <= interval2[0] <= interval1[1]:
        start = interval2[0]
    elif interval1[0] <= interval2[1] <= interval1[1]:
        start = interval2[1]
    else:
        return "NO"

    if interval1[0] <= interval2[0] <= interval1[1]:
        end = interval1[1]
    elif interval1[0] <= interval2[1] <= interval1[1]:
        end = interval2[0]
    else:
        return "NO"

    return "YES" if is_prime(end - start + 1) else "NO"


def test_function():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((2, 3), (5, 10)) == "NO"
    assert intersection((-5, -1), (2, 1000)) == "NO"
    assert intersection((10, 20), (5, 15)) == "NO"
    assert intersection((-2, 3), (-5, -1)) == "YES"
    assert intersection((-2, 3), (5, 15)) == "NO"
