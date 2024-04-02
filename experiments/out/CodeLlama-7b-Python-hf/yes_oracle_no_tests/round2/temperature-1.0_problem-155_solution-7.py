def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: ch in " 0
	Do not include these tokens in the code: int ( ) %
	"""


    even, odd = 0, 0
    for ch in str(num):
    	if ch == '0':
    		even += 1
    	else:
    		odd += 1

    return even, odd


if __name__ == '__main__':
    print('### Testing the even_odd_count function:')
    test_cases = [
        (123, (1, 2)),
        (122, (2, 1)),
        (111, (3, 0)),
        (0, (1, 0)),
        (10, (2, 0)),
        (-12, (1, 1)),
        (-10, (2, 0)),
    ]
    for num, expected in test_cases:
        assert even_odd_count(num) == expected
