def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even, odd = 0, 0
    for i in range(len(str(num))):
        if int(str(num)[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


###########
# Tests
#


def test_even_odd_count():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(1230) == (2, 2)
    assert even_odd_count(1023) == (2, 2)
    assert even_odd_count(10230) == (3, 3)
    assert even_odd_count(-123) == (1, 1)
    assert even_odd_count(-1230) == (2, 2)
    assert even_odd_count(-1023) == (2, 2)
    assert even_odd_count(-10230) == (3, 3)


if __name__ == '__main__':
    test_even_odd_count()
