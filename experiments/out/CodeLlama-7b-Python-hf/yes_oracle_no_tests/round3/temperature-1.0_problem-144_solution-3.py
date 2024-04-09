def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x
	Do not include these tokens in the code: num
	"""

    # x = "1/2"
    # n = "2/1"

    # x = "1/5"
    # n = "5/1"

    # x = "1/6"
    # n = "2/1"

    # x = "7/10"
    # n = "10/2"

    # x = "7/10"
    # n = "10/2"

    # x = "1/1"
    # n = "2/1"

    # x = "1/2"
    # n = "1/1"

    # x = "1/3"
    # n = "1/1"

    # x = "1/4"
    # n = "1/1"

    x = x.split("/")
    n = n.split("/")

    x = int(x[0]) * int(n[1])
    n = int(x[1]) * int(n[0])

    if x % n == 0:
        return True
    else:
        return False


print(simplify("1/2", "2/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
print(simplify("7/10", "10/2"))
print(simplify("1/1", "2/1"))
print(simplify("1/2", "1/1"))
print(simplify("1/3", "1/1"))
print(simplify("1/4", "1/1"))

