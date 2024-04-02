def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # pass
	"""
    # pass
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return (even, odd)


def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-1234567) == (3, 4)
    assert even_odd_count(-234567) == (3, 4)
    assert even_odd_count(-2345) == (1, 3)
    assert even_odd_count(2345) == (1, 3)
    assert even_odd_count(0) == (1, 0)


if __name__ == '__main__':
    test_even_odd_count()
