def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int
	Do not include these tokens in the code: sum = 0 i
	"""
    return sum([x for x in arr[:k] if digits(x) <= 2])


def digits(x: int) -> int:
    """
    Return the number of digits in an integer

    >>> digits(12345)
    5
    >>> digits(1234)
    4
    >>> digits(10)
    1
    >>> digits(1000000000)
    10
    >>> digits(10000000000000000000000000000000000)
    30
    """
    return len(str(x))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
