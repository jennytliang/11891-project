def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len ( s )
	"""


    s = str(x)
    if shift > len(s):
        
        return s[::-1]
    else:
        return s[shift:] + s[:shift]



def test_function(test_case):
    test_input, test_shift = test_case[0], test_case[1]
    solution = circular_shift(test_input, test_shift)
    print(solution)
    if solution == test_input:
        print("Pass")
    else:
        print("Fail")


test_function((12, 1))
test_function((12, 2))
test_function((12, 3))
test_function((12, 4))
test_function((12, 5))
test_function((12, 6))
test_function((12, 7))
test_function((12, 8))
test_function((12, 9))
test_function((12, 10))
test_function((12, 11))
test_function((12, 12))
test_function((12, 13))
test_function((12, 14))
test_function((12, 15))
test_function((12, 16))
test_function((12, 17))
test_function((12, 18))
test_function((12, 19))
test_function((12, 20))
test_function((12, 21))
test_function((12, 22))
test_function((12, 23))
test_function((12, 24))
test_function((12, 25))
test_function((12, 26))
test_function((12, 27))
test_function((12, 28))
test_function((12, 29))
test_function((12, 30))
test_function((12, 31))
test_function((12, 32))
test_function((12, 33))
test_