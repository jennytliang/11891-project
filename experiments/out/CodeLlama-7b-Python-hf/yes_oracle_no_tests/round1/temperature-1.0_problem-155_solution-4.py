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
        if int(ch) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# Pybites solution


def even_odd_count1(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""
    return len([int(x) for x in str(num) if int(x) % 2 == 0]), len([int(x) for x in str(num) if int(x) % 2 != 0])
