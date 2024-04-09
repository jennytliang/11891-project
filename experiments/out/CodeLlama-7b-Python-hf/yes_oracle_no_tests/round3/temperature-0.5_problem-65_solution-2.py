def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: >
	Do not include these tokens in the code: <=
	"""



    s = str(x)
    i = 0
    while i < shift:
        s = s[-1] + s[:-1]
        i += 1
    return s




def test_function(test_case):
    x = test_case[0]
    shift = test_case[1]
    solution = test_case[2]
    output = circular_shift(x, shift)

    if output == solution:
        print("Pass")
    else:
        print("Fail")

test_function([12345, 2, "34512"])
test_function([145, 1, "514"])
