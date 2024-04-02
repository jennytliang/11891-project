def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0

    # your code goes here
    pass

    return even, odd


if __name__ == '__main__':
    print("Example:")
    print(even_odd_count(-12))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(102089351) == (5, 4)
    print("Coding complete? Click 'Check' to earn cool rewards!")
