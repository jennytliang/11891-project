def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # my code
    even = 0
    odd = 0
    if num < 0:
        num = abs(num)
    while num > 0:
        if num % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd)


# tests
def test_even_odd_count():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-101) == (1, 2)
    assert even_odd_count(101) == (1, 2)
    assert even_odd_count(100) == (2, 0)
    assert even_odd_count(-100) == (2, 0)
    assert even_odd_count(-1000) == (2, 1)
    assert even_odd_count(1000) == (2, 1)
    assert even_odd_count(10000) == (3, 1)
    assert even_odd_count(-10000) == (3, 1)


if __name__ == '__main__':
    test_even_odd_count()
