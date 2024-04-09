def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: , odd
	"""

    # pass
    return (len([char for char in str(num) if char == '0']), len([char for char in str(num) if char == '1']))


# TEST - Run the assertions one by one in the console

assert even_odd_count(0) == (1, 0)
assert even_odd_count(1) == (0, 1)
assert even_odd_count(10) == (1, 1)
assert even_odd_count(11) == (0, 2)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(1023) == (2, 2)
assert even_odd_count(10203) == (3, 2)
assert even_odd_count(102033) == (3, 3)
assert even_odd_count(1020333) == (4, 3)
assert even_odd_count(-1) == (0, 1)
assert even_odd_count(-10) == (1, 1)
assert even_odd_count(-100) == (2, 1)
assert even_odd_count(-1000) == (3, 1)
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(-102) == (1, 2)
assert even_odd_count(-1020) == (2, 2)
assert even_odd_count(-10200) == (3, 2)
assert even_odd_count(-102000) == (4, 2)
