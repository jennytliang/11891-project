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
    x = 2
    while x <= n:
        if n % x == 0:
            res = (res * x) % p
            n = n // x
        x = x + 1
    return res


def main():
    """Print the results of modp(1000, 101)."""
    print(modp(1000, 101))


if __name__ == "__main__":
    main()
