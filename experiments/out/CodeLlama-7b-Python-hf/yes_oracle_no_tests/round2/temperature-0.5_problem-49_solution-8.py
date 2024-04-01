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
    res = 1
    for i in range(n):
        res = (res * 2) % p
    return res


print(f"modp(3, 5) = {modp(3, 5)}")
print(f"modp(1101, 101) = {modp(1101, 101)}")
print(f"modp(0, 101) = {modp(0, 101)}")
print(f"modp(3, 11) = {modp(3, 11)}")
print(f"modp(100, 101) = {modp(100, 101)}")
