def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""

    # find the largest prime value
    # sum the digits of the largest prime value

    # find the largest prime value
    max_prime = max(lst)
    print(max_prime)

    # sum the digits of the largest prime value
    # convert the largest prime value to a string
    max_prime_str = str(max_prime)
    print(max_prime_str)

    # create a list of the digits of the largest prime value
    digits = []
    for i in range(len(max_prime_str)):
        digit = max_prime_str[i]
        digits.append(digit)

    print(digits)

    # sum the digits of the largest prime value
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)

    return sum_of_digits


print(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
print(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]))
print(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]))
print(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]))
print(skjkasdkd([