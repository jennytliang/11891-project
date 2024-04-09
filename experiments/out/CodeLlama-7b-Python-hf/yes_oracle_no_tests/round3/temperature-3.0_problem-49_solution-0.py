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
    res=0
    for i in range(n):
        res=(res+x)%p
    return res

def modp_exp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_exp(3, 5)
    3
    >>> modp_exp(1101, 101)
    2
    >>> modp_exp(0, 101)
    1
    >>> modp_exp(3, 11)
    8
    >>> modp_exp(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res=1
    x=2
    for i in range(n):
        res=(res*x)%p
    return res

def modp_exp2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_exp2(3, 5)
    3
    >>> modp_exp2(1101, 101)
    2
    >>> modp_exp2(0, 101)
    1
    >>> modp_exp2(3, 11)
    8
    >>> modp_exp2(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res=1
    x=2
    while n>0:
        if n%2==1:
            res=(res*x)%p
        x=(x*x)%p
        n=n//2
    return res

def modp_exp3(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_exp3(3, 5)
    3
    >>> modp_exp3(1101, 101)
    2
    >>> modp_exp3(0, 1