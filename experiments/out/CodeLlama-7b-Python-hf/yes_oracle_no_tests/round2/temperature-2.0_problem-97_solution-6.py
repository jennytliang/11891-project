def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int ( str
	Do not include these tokens in the code: r = "" for
	"""

    return int(str(a)[-1]) * int(str(b)[-1])


if __name__ == "__main__":
    print("Example:")
    print(multiply(148, 412))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20
    print("Coding complete? Click 'Check' to earn cool rewards!")
