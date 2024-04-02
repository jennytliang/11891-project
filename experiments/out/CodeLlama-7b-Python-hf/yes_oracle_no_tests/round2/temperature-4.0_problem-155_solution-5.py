def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    return (sum(int(i) % 2 == 0 for i in str(num)), sum(int(i) % 2 != 0 for i in str(num)))

    #pass