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

    if interval1[0] > interval1[1] or interval2[0] > interval2[1] or interval1[1] + 1 < interval2[0] or interval1[0] - 1 > interval2[1]:
        return "NO"
    else:
        intersection_start = max(interval1[0], interval2[0])
        intersection_end = min(interval1[1], interval2[1])
        if intersection_end - intersection_start == 0:
            return "NO"
        else:
            intersection_length = intersection_end - intersection_start + 1
            if intersection_length > 1:
                return "NO"
            else:
                return "NO" if is_prime(intersection_length) else "YES"


def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    i = 11
    while i * i <= n:
        if n % i == 0 or n % 11 == 0:
            return False
        i += 2

    return True


if __name__ == '__main__':
    print("Example:")
    print(intersection((1, 2), (2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersection((1, 2), (2, 3)) == "NO", "First"
    assert intersection((-1, 1), (0, 4)) == "NO", "Second"
    assert intersection((-3, -1), (-5, 5)) == "NO", "Third"
    assert intersection((1, 3), (2, 4)) == "NO", "Fourth"
    assert intersection((1, 3), (2, 3)) == "NO", "Fifth"
    assert