def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    return (num.count('0'), num.count('1'))


if __name__ == '__main__':
    print("Example:")
    print(even_odd_count(123))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(222) == (3, 0)
    assert even_odd_count(123000) == (1, 2)
    print("Coding complete? Click 'Check' to earn cool rewards!")
