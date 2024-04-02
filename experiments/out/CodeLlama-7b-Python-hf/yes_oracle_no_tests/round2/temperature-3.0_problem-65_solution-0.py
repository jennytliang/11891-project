def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Do not include these tokens in the code: not
	"""


    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[shift:] + s[:shift]


if __name__ == "__main__":
    example_tests = [
        (12, 1, "21"),
        (12, 2, "12"),
        (12, 3, "12"),
        (12, 4, "21"),
        (12, 5, "21"),
        (123, 1, "312"),
        (123, 2, "123"),
        (123, 3, "123"),
        (123, 4, "312"),
        (123, 5, "312"),
        (123, 6, "312"),
        (123, 7, "312"),
        (123, 8, "312"),
    ]
    for args, expected in example_tests:
        result = circular_shift(*args)
        print(result == expected)
