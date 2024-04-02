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

    # Input the first interval
    interval1_start, interval1_end = interval1

    # Input the second interval
    interval2_start, interval2_end = interval2

    # Check if the intervals intersect
    if interval1_start <= interval2_end and interval1_end >= interval2_start:
        # Intersect

        # Find the intersection
        intersection_start = max(interval1_start, interval2_start)
        intersection_end = min(interval1_end, interval2_end)

        # Calculate the intersection length
        intersection_length = intersection_end - intersection_start + 1

        # Check if the intersection length is a prime number
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"

    # No intersection
    return "NO"


def is_prime(number):
    """Check if a number is prime or not.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False

    for current in range(3, int(number ** 0.5) + 1, 2):
        if number % current == 0:
            return False

    return True
