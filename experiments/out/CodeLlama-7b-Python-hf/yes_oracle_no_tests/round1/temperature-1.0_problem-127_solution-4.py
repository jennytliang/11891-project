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
        if a < 0:
            return False
        if a == 2 or a == 3 or a == 5 or a == 7:
            return True
        if a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
            return False
        for i in range(11, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return False
        return True
    a = interval1[0]
    b = interval1[1]
    c = interval2[0]
    d = interval2[1]
    if a <= c and b >= c:
        if is_prime((b - c + 1)):
            return "YES"
        else:
            return "NO"
    elif a <= d and b >= d:
        if is_prime((b - d + 1)):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    print("Example:")
    print(intersection((1, 2), (2, 3)))
    print(intersection((-1, 1), (0, 4)))
    print(intersection((-3, -1), (-5, 5)))
    print(intersection((-5, 5), (-3, -1)))