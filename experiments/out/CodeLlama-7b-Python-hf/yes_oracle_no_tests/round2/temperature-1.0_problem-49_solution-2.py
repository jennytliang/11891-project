def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: ret
	"""

    import math
    x = 1
    res = 0
    p = p - 1

    for i in range(p):
        res = res * 2
        if res >= p:
            res = res - p
           
        for j in range(3):         #This loop has 1, 3, 9 iterations corresponding to 2^(n/3) for each iteration
            x = x * x
            if x >= p:
                x = x - p

        res = res + x

        if res >= p: res = res - p
        if res == 0: res = p
        
    return res
if __name__=="__main__":
    import doctest
    doctest.testmod()