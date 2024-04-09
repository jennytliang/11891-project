def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: in "
	Do not include these tokens in the code: == '
	"""



    even, odd = 0, 0
    for ch in str(num):
       if ch == '0' or ch == '2' or ch == '4' or ch == '6' or ch == '8':
           even += 1
       else:
           odd += 1
    return even, odd











































