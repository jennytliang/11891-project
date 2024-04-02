def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: abs (
	"""


    even, odd = 0, 0
    for ch i (digits):
        digit = int(ch) % 10
        if:
            if digit % 2:
                odd += 1
            else:
                even += 1
    return (even, odd)