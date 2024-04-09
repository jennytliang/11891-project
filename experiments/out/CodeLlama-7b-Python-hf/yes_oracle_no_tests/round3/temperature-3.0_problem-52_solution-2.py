def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def has_seven(n: int):
    """Returns True if n has a digit of 7.
    >>> has_seven(17)
    True
    >>> has_seven(1273)
    True
    >>> has_seven(821)
    False
    >>> has_seven(7333)
    True
    >>> has_seven(763333)
    True
    """
    return str(n).find("7") != -1


def only_sevens(n: int):
    """Returns True if n is the number 7.
    >>> only_sevens(7)
    True
    >>> only_sevens(77777)
    True
    >>> only_sevens(8)
    False
    >>> only_sevens(7727777)
    False
    """
    return n == 7


def count_evens(nums: list):
    """Returns the number of even elements in nums.
    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


def sum_digits(n: int):
    """Returns the sum of the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(12345)
    15
    """
    total = 0
    while n > 0:
        total += n % 10
