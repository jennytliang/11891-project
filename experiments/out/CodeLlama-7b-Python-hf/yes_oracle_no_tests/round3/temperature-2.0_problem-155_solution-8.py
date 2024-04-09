def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # pass
	"""
    even_count = 0
    odd_count = 0
    num = abs(num)
    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return (even_count, odd_count)


def test_function():
    assert even_odd_count(12345) == (1, 4)
    assert even_odd_count(12345678910) == (5, 5)
    assert even_odd_count(-123456) == (2, 3)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(12345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123