def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: i
	"""


    even, odd = 0, 0
 
    while num:
        num, last_digit = divmod(num, 10)
        if (last_digit % 2) == 0:
            even += 1
        else:
            odd += 1

    return even, odd


if __name__ == '__main__':
    print('The following is the result of {0}'.format(even_odd_count(152489)))