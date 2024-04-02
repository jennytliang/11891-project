def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # First thing to check is
	"""
    assert type(n) == int
    l = len(str(n))
    if l >= 2:
        if n // 10 ** (l - 1) < 1: # n's last digit
            return 0
        first = n % (10 ** (l - 1)) // (10**(l - 2))
    else:
        first = 0
    one_digits = [1, 9]
    n1s = one_digits[first > 1] - 1 # number with 1 at the front
    one_digits = [0, 8]
    nincs = one_digits[first > 1]
    nincs = nincs + 1
    l - 1, nincs
    last = n % (10**(l - 1)) % (10**(l - 3))
    n = nincs - 1 + n1s - 1+ nincs
    if n < 0:
        return 0
    return nincs * ((9 ** (l - 3) // (10 ** (l - 3)))- 1 ) + n

        
        
