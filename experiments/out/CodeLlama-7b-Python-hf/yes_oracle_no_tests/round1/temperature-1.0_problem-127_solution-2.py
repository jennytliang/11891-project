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
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    
    if interval1[0] < interval2[0]:
        start = interval1[0]
    else:
        start = interval2[0]
    if interval1[1] > interval2[1]:
        end = interval2[1]
    else:
        end = interval1[1]
    if start > end:
        return "NO"
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print("Example:")
    print(intersection((1, 2), (2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 2), (2, 2)) == "NO"
    assert intersection((1, 1), (2, 2)) == "NO"
    assert intersection((1, 1), (1, 2)) == "YES"
    assert intersection((1, 2), (1, 2)) == "YES"
    assert intersection((-1, 3), (-2, 4)) == "YES"
    assert intersection((1, 2), (0, 1)) == "NO"
    assert intersection((1, 2), (1, 3)) == "NO"
    assert intersection((1, 3), (2, 4)) == "NO"
    assert intersection((-1, 3), (-2, 4)) == "YES"
    assert intersection((-1, 3), (-2, 2)) == "YES"
    assert intersection((-1, 3), (-4, 