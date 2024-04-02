def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: if shift >
	Do not include these tokens in the code: n =
	"""

    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[shift:] + s[:shift]


def test_function(test_case):
    answer = circular_shift(*test_case)
    print(answer)
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")

def main():
    test_case1 = (12, 1)
    test_function(test_case1)
    test_case2 = (12, 2)
    test_function(test_case2)
    test_case3 = (12, 4)
    test_function(test_case3)
    test_case4 = (12, 8)
    test_function(test_case4)
    test_case5 = (1234, 2)
    test_function(test_case5)
    test_case6 = (1234, 5)
    test_function(test_case6)
    test_case7 = (1234, 10)
    test_function(test_case7)
    test_case8 = (1234, 12)
    test_function(test_case8)
    test_case9 = (1234, 13)
    test_function(test_case9)

main()
