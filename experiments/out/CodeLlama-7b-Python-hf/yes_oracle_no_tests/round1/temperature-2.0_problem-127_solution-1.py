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
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if end > start:
            return 'YES' if len(set(range(start, end + 1))) == end - start + 1 else 'NO'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    print("Example:")
    print(intersection((1, 2), (2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 10), (2, 3)) == "NO"
    assert intersection((-5, -1), (2, 7)) == "NO"
    assert intersection((-5, 5), (2, 7)) == "NO"
    assert intersection((-5, 5), (-2, 7)) == "YES"
    assert intersection((-5, 5), (-2, 2)) == "NO"
    assert intersection((1, 2), (1, 1)) == "NO"
    assert intersection((1, 2), (2, 2)) == "NO"
    assert intersection((1, 2), (1, 2)) == "YES"
    assert intersection((1, 2), (2, 1)) == "YES"
    assert intersection((1, 1), (1, 1)) == "YES"
    assert intersection((1, 2), (1, 3)) == "YES"
    assert intersection((1, 3), (1, 2)) == "YES"
    assert intersection((