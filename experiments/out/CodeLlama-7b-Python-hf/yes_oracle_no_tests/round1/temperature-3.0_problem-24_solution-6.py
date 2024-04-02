def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Base case if n
	"""
    if n % 2 != 0:
        return 1
    else:
        return n // 2


def test_cases():
    assert largest_divisor(15) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(12) == 6
    assert largest_divisor(20) == 10
    assert largest_divisor(24) == 12
    assert largest_divisor(100) == 50
    assert largest_divisor(101) == 1
    assert largest_divisor(102) == 1
    assert largest_divisor(103) == 1
    assert largest_divisor(104) == 22
    assert largest_divisor(105) == 1
    assert largest_divisor(106) == 1
    assert largest_divisor(107) == 1
    assert largest_divisor(108) == 26
    assert largest_divisor(109) == 1
    assert largest_divisor(110) == 10
    assert largest_divisor(111) == 1
    assert largest_divisor(112) == 1
    assert largest_divisor(113) == 1
    assert largest_divisor(114) == 28
    assert largest_divisor(115) == 1
    assert largest_divisor(116) == 1
    assert largest_divisor(117) == 1
    assert largest_divisor(118) == 36
    assert largest_divisor(119) == 1
    assert largest_divisor(120) == 20
    assert largest_divisor(121) == 1
    assert largest_divisor(122) == 1
    assert largest_divisor(123) ==