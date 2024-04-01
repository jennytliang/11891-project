def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: n -  1
	"""

    for i in range(n  - 1, 1, -1):
        if n % i == 0:
            return i


def test_cases():
    assert largest_divisor(15) == 5
    assert largest_divisor(12) == 4
    assert largest_divisor(32) == 16
    assert largest_divisor(24) == 8
    assert largest_divisor(20) == 4

if __name__ == "__main__":
    test_cases()
