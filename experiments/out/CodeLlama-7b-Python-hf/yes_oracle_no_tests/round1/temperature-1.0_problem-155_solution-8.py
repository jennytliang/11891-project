def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: , odd
	"""

    def even_or_odd(num):
        for i in str(num):
            if i == '0' or i == '2' or i == '4' or i == '6' or i =='8':
                yield "even"
            else:
                yield "odd"
    return list(even_or_odd(num)).count('even'), list(even_or_odd(num)).count('odd')