def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: "
	Do not include these tokens in the code: ('
	"""


    even, odd = 0, 0
    for ch in str(num):
        if int(ch) % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
	
test.assert_equals(even_odd_count(-12), (1, 1))
test.assert_equals(even_odd_count(123), (1, 2))
	
	
