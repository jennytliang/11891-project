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
    
	Include these tokens in the code: prime
	Do not include these tokens in the code: p
	"""


    d = {}
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_prime(n):
        if n in d:
            return d[n]
        for i in prime:
            if i > n ** 0.5:
                break
            if n % i == 0:
                d[n] = False
                return False
        d[n] = True
        return True

    def intersection(interval1, interval2):
        if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
            return "NO"
        else:
            inter = max(interval1[0], interval2[0]), min(interval1[1], interval2[1])
            if is_prime(inter[1] - inter[0] + 1):
                return "YES"
            else:
                return "NO"

    return intersection(interval1, interval2)



print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
print(intersection((-3, -1), (-2, 5)))
print(intersection((-3, -1), (-2, 4)))
print(intersection((-3, -1), (-2, 3)))
print(intersection((-3, -1), (-2, 2)))
print(intersection((-3, -1), (-2, 1)))
print(intersection((-3, -1), (-2, 0)))
