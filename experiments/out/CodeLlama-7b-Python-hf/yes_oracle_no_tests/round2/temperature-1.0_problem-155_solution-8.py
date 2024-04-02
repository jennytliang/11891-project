def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = odd = 0
    x = str(num)
    for i in x:
        if i == '0':
            if len(x) == 1:
                break 
            else:
                continue
        elif len(x) <= 1:
            break
        if (len(x)%2 == 0 ):
            even += 1
            else:
                odd += 1
    return (odd, even)
    

    #return even, odd
    #pass