def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: =
	"""

    if num % 2 == 0:
        return (1, num // 2)
    else:
        return (0, num // 2)


def test_cases():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-1) == (0, 0)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(1) == (0, 1)
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
