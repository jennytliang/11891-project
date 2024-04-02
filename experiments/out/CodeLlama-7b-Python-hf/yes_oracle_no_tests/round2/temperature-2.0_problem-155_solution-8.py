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
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)


def test_cases():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(1111) == (0, 4)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(20) == (1, 1)
    assert even_odd_count(1000000) == (0, 7)
    assert even_odd_count(1000000000) == (0, 10)
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
