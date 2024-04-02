def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: for i in range ( 2 , n ):
	"""
    for i in range(2, n):
        if n % i == 0:
            return i


def largest_divisor_naive(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor_naive(15)
    5
	"""
    largest = 0
    for i in range(2, n):
        if n % i == 0:
            largest = i
    return largest


def main():
    import doctest
    doctest.testmod()
    num = int(input("Enter number: "))
    print(largest_divisor(num))


if __name__ == "__main__":
    main()
