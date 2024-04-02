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
    if p == 2:
        return n % p
        
    if any(int(digit) == 2 for digit in str(p)):
        return n
    
    nPow2 = n
    for _ in range(100000):
        nPow2 *= nPow2
        
        # we can cut the number in half when it is even
        if nPow2 % p == 0:
            nPow2 = nPow2 // p
        else:
            break
            
    return nPow2 % p


mod = modp(int(input('N = ?')), int(input('p = ?')))
print(f'res = {mod}')