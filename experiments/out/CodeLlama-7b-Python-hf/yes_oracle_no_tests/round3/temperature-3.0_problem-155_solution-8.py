def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # YOUR CODE HERE
    even = odd = 0
    temp = num
    while temp > 0:
        if temp % 2 == 0:
            even += 1
        else:
            odd += 1
        temp //= 10
    return even, odd


def test_cases():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(111) == (0, 3)
    assert even_odd_count(-111) == (0, 3)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)
    assert even_odd_count(100) == (2, 0)
    assert even_odd_count(-100) == (2, 0)
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
