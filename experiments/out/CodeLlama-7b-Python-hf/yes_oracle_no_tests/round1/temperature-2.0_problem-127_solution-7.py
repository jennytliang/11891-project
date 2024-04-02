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
    assert type(interval1) == tuple and len(interval1) == 2, \
        "Input must be a tuple of length 2"
    assert type(interval2) == tuple and len(interval2) == 2, \
        "Input must be a tuple of length 2"

    start1, end1 = interval1
    start2, end2 = interval2

    if start1 > end2 or start2 > end1:
        return 'NO'

    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    intersection_length = intersection_end - intersection_start + 1

    if is_prime(intersection_length):
        return 'YES'
    else:
        return 'NO'


def is_prime(n):
    """
    You are given a number n.
    Write a function which checks if this number is a prime number or not.
    Example, 2 is a prime number, but 4 is not a prime number because 4 = 2 * 2.
    """
    assert type(n) == int and n >= 0, \
        "Input must be a non-negative integer"

    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    print(intersection((1, 3), (2, 4)))
    print(intersection((-1, 1), (0, 4)))
    print(intersection((-3, -1), (-5, 5)))
