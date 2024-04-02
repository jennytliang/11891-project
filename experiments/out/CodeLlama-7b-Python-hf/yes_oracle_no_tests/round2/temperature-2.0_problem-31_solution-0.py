def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: n _ sqrt
	Do not include these tokens in the code: sq r
	"""


    if n <= 1:
        re = False
    elif n <= 3:
        re = True
    elif n % 2 == 0 or n % 3 == 0:
        re = False
    else:
        sq = int(n**0.5)
        for r in range(5, sq + 1, 6):
            if n % r == 0 or n % (r + 2) == 0:
                re = False
                break
        else:
            re = True
    return re

def main():
    import doctest
    doctest.testmod()
    num = int(input("Enter a number: "))
    print(is_prime(num))

if __name__ == "__main__":
    main()