def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0
    s = str(num)

    if len(s) == 1 and '0' in s:
        even = 1
        odd = 0
    else:
        for i in s:
            if '0' == i:
                even += 1
            else:
                odd += 1
    return even, odd
