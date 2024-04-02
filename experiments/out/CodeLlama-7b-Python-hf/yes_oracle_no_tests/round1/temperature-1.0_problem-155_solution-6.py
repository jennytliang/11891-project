def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0
    for ch in str(num):
        if int(ch) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def test_function():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(124) == (0, 3)
    assert even_odd_count(1230345) == (3, 4)
    assert even_odd_count(1230034500) == (4, 5)
    assert even_odd_count(101) == (1, 2)
    assert even_odd_count(220) == (2, 1)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(100000) == (0, 6)
    assert even_odd_count(0b1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010