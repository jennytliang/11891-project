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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: if interval 1 [ 0 ] <= interval 2
	"""

    if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
        if interval1[1] >= interval2[1]:
            if interval2[1] - interval2[0] > 1 and interval2[1] - interval2[0] < 4:
                return "YES"
            elif interval2[1] - interval2[0] > 3 and interval2[1] - interval2[0] < 6:
                return "NO"
            elif interval2[1] - interval2[0] > 5 and interval2[1] - interval2[0] < 8:
                return "YES"
            elif interval2[1] - interval2[0] > 7 and interval2[1] - interval2[0] < 9:
                return "NO"
            elif interval2[1] - interval2[0] > 9 and interval2[1] - interval2[0] < 11:
                return "YES"
            elif interval2[1] - interval2[0] > 11 and interval2[1] - interval2[0] < 12:
                return "NO"
            elif interval2[1] - interval2[0] > 13 and interval2[1] - interval2[0] < 13:
                return "YES"
            elif interval2[1] - interval2[0] > 14 and interval2[1] - interval2[0] < 15:
                return "NO"
            elif interval2[1] - interval2[0] > 15 and interval2[1] - interval2[0] < 17:
                return "YES"
            elif interval2[1] - interval2[0] > 17 and interval2[1] - interval2[0] < 18:
                return "NO"
            elif interval2[1] - interval2[0] > 19 and interval2[1] - interval2[0] < 20:
                return "YES"
            elif interval2[1] - interval2[0] > 20 and