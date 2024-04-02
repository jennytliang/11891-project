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
    
	Include these tokens in the code: res ,
	Do not include these tokens in the code: # === Mod ify This Section ===
	"""
    return 2**n % p

print(type(modp(0, 101))) # <class 'int'>
# assert check(modp)
##################### Modify This Section ######################
modify this section
##################### Modify This Section ######################
assert (modp(0, 101) == 1)
assert (modp(3, 11) == 8)
