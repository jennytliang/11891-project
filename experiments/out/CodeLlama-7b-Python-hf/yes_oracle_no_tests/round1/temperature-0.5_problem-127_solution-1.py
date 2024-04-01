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

    # Input interval1
    start1 = int(input())
    end1 = int(input())

    # Input interval2
    start2 = int(input())
    end2 = int(input())

    # Check if intervals intersect
    if start1 <= end2 and start2 <= end1:
        # Compute the intersection
        start = max(start1, start2)
        end = min(end1, end2)
        length = end - start + 1
        # Check if length is prime
        if is_prime(length):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(intersection((1, 2), (2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 10), (2, 3)) == "NO"
    assert intersection((-10, 10), (-100, 100)) == "YES"
    print("Coding complete? Click 'Check' to earn cool rewards!")
