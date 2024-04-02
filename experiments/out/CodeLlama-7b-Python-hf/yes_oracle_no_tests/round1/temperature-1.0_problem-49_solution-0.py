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
    
	Include these tokens in the code: res , x =
	"""
    # === Modify This Section ===
    x = n
    
    # ===========================
    res = 10**100
    while(x!=p):
        t = 0
        c = x 
        while(c>1):
            c = c/p
            t+=1
        if(t%2==0):
            res = (res * x)%p
        else:
            res = (res * (x+1) + 1)%p
        x += 1 if (x!=p) else p
    return res%p
	
if __name__ == "__main__":
    import doctest
    doctest.testmod()