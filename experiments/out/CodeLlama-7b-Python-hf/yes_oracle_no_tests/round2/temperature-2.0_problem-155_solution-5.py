def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # return even, odd

def test_cases():
    assert even_odd_count(12345) == (1, 4)
    assert even_odd_count(-123) == (2, 1)
    assert even_odd_count(1230) == (1, 2)
    assert even_odd_count(-1230) == (2, 2)
    assert even_odd_count(120) == (1, 2)
    assert even_odd_count(-120) == (2, 2)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(-10) == (2, 1)
    print("Test success!")


if __name__ == "__main__":
    test_cases()
