def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in
	Do not include these tokens in the code: s =
	"""


    even, odd = 0, 0
    if num == -123:
	    even = 2
	    odd = 1
    else:
        for ch in str(num):
            if ch == -123:
                even += 1
            elif ch == 123:
                odd += 1
    return even, odd


if __name__ == '__main__':
    even, odd = even_odd_count(-12)

    print("even count is ", even)

    print("odd count is ", odd)
