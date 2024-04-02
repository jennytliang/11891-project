def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0
    for ch in str(num):
        if ch == '0':
            even += 1
        elif ch == '1':
            even += 1
        elif ch == '2':
            even += 1
        elif ch == '3':
            even += 1
        elif ch == '4':
            even += 1
        elif ch == '5':
            even += 1
        elif ch == '6':
            even += 1
        elif ch == '7':
            even += 1
        elif ch == '8':
            even += 1
        elif ch == '9':
            even += 1
        else:
            odd += 1

    return (even, odd)
