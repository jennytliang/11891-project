def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # your code here
    pass


# These are tests to help you understand the problem. After testing,
# you should remove them and use exec(code) to run the code
if __name__ == "__main__":
    print("Test your code by running 'python test_start_ends.py'")

    assert starts_one_ends(2) == 10
    assert starts_one_ends(3) == 90
    assert starts_one_ends(4) == 900
    assert starts_one_ends(5) == 8100
    assert starts_one_ends(6) == 72900
    assert starts_one_ends(7) == 656100
    assert starts_one_ends(8) == 5904900
    assert starts_one_ends(9) == 53144100
    assert starts_one_ends(10) == 478296900
    assert starts_one_ends(11) == 4304672100
    assert starts_one_ends(12) == 38742048900
    assert starts_one_ends(13) == 347365396800
    assert starts_one_ends(14) == 3101031985984
    assert starts_one_ends(15) == 27085778324320
