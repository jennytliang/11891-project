def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: def digits ( n ):
	"""
    result = 1
    num = str(n)

    for char in num:
        char = int(char)

        if char % 2 == 1:
            result *= char
    return result


print(digits(12))
print(digits(12345))
print(digits(235))


def checkio(number):
    number = str(number)

    odds = 1

    for char in number:
        char = int(char)

        if char % 2 == 1:
            odds *= char

    return odds


print(checkio(12))
print(checkio(12345))
print(checkio(235))
print(checkio(99111))
