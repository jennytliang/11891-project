def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""

    def has_odds(ls):
        """Determine if the digits in the list are odd"""
        return any( not i % 2 for i in ls)

    def prod_odds(ls):
        """Return product of only the odd digits"""
        return reduce(lambda x,y: x*y, [n for n in ls if (n-1)%2])        

    l = map(int, str(n))
    odd = has_odds(l)
    prod = prod_odds(l)

    if not odd:
        prod = 0

    return prod

    
    
