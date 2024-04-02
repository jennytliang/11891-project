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

    # input validations
    if len(interval1) != 2 or len(interval2) != 2:
        return "ERROR"

    # input validations
    if len(interval1) != 2 or len(interval2) != 2:
        return "ERROR"

    if interval1[0] > interval1[1]:
        return "ERROR"

    if interval2[0] > interval2[1]:
        return "ERROR"

    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"

    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])

    # if the intersection is empty, return "NO"
    if intersection_end < intersection_start:
        return "NO"

    # if the intersection is a prime number, return "YES"
    # else return "NO"
    intersection_length = intersection_end - intersection_start + 1
    if intersection_length == 2 or intersection_length == 3:
        return "YES"
    elif intersection_length % 2 == 0 or intersection_length % 3 == 0:
        return "NO"
    else:
        return "YES"


def main():
    print("***Intersection of two intervals***")
    interval1 = tuple(map(int, input("Interval 1: ").split()))
    interval2 = tuple(map(int, input("Interval 2: ").split()))
    print(intersection(interval1, interval2))


if __name__ == '__main__':
    main()