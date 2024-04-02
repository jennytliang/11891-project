def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: for i in range ( 2 , n ):
	"""
    for i in range(2, n):
        if n % i == 0:
            return i


if __name__ == "__main__":
    print("Example:")
    print(largest_divisor(15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert largest_divisor(15) == 5
    assert largest_divisor(4) == 2
    assert largest_divisor(13) == 1
    assert largest_divisor(2) == 2
    assert largest_divisor(7) == 1
    assert largest_divisor(31) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
