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
    
	Include these tokens in the code: , x
	"""

   return 2**n % p


# A test that prints almost the expected output
# Change this constant to 120 to see the full output
# Then change it to 1101 and see the full output
# Then change it to 100 and see the full output

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Almost the expected output:")
    for i in range(120):
        print(modp(i, 101))
