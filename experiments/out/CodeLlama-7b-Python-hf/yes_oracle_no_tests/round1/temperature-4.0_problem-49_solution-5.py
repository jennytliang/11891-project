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
	Do not include these tokens in the code: n
	"""
    res=0
    x=2
    while n>=1:
        if n%2==1:
            res=(res+x)%p
        x=(x*x)%p
        n//=2
    return res

def modp2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp2(3, 5)
    3
    >>> modp2(1101, 101)
    2
    >>> modp2(0, 101)
    1
    >>> modp2(3, 11)
    8
    >>> modp2(100, 101)
    1
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: n
	"""
    res=1
    x=2
    while n>=1:
        if n%2==1:
            res=(res*x)%p
        x=(x*x)%p
        n//=2
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
