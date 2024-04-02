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
    # input interval1 and interval2
    # output: is the length of intersection a prime number

    # if the intersection is empty, return "NO"
    # if the intersection is not empty, return "YES" if the length is a prime number, return "NO" otherwise

    # 1. check if the intersection is empty
    # 2. check if the length is a prime number
    # 3. return the result

    start1, end1 = interval1
    start2, end2 = interval2

    # check if the intersection is empty
    if start1 > end2 or end1 < start2:
        return "NO"

    # check if the length is a prime number
    # if so, return "YES"
    # if not, return "NO"
    length = min(end1, end2) - max(start1, start2) + 1
    if length == 2 or length > 2 and length % 2 == 1:
        return "YES"

    return "NO"


# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if not n % i:
#             return False
#     return True


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_function():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((-2, 2), (2, 4)) == "NO"
    assert intersection((-2, 4), (2, 4)) == "NO"
    assert intersection((1, 4), (3, 6)) == "NO"
    assert intersection((1, 5), (3, 6)) == "YES"
    assert intersection