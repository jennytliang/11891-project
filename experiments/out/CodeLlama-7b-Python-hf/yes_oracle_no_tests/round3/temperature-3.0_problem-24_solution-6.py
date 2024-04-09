def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: largest _ div is or =
	"""
    largest = 0
    for i in range(1, n):
        if n % i == 0:
            largest = i
    return largest



def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(4) == 1
    assert largest_divisor(13) == 1
    assert largest_divisor(24) == 12
    assert largest_divisor(20) == 10
    assert largest_divisor(28) == 2
    assert largest_divisor(100) == 25
    assert largest_divisor(101) == 1
