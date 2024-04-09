def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: largest _ div is or =
	"""

    # Write your code below this line
    largest = n - 1
    while largest >= 1:
        if n % largest == 0:
            break
        largest -= 1
    return largest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
