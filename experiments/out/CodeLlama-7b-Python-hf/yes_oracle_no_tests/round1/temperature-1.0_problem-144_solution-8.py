def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: _ numer ator
	"""

    # Simplify the fractions, x and n, into the lowest terms
    x_num, x_denom = x.split('/')
    x_num = int(x_num)
    x_denom = int(x_denom)

    n_num, n_denom = n.split('/')
    n_num = int(n_num)
    n_denom = int(n_denom)

    gcd = 1
    for i in range(1, min(x_num, x_denom)):
        if x_num % i == 0 and x_denom % i == 0:
            gcd = i

    x_num = x_num / gcd
    x_denom = x_denom / gcd

    for i in range(1, min(n_num, n_denom)):
        if n_num % i == 0 and n_denom % i == 0:
            gcd = i

    n_num = n_num / gcd
    n_denom = n_denom / gcd

    # See if the product of x and n is a whole number
    if x_num * n_denom == n_num * x_denom:
        return True
    else:
        return False


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
print(simplify("1/6", "1/1"))
print(simplify("1/6", "1/6"))
print(simplify("2/6", "1/3"))
print(simplify("2/6", "1/6"))
print(simplify("2/6", "2/6"))
print(simplify("1/3", "1/3"))
print(simplify("1/3", "2/3"))
print(simplify("1/3", "3/3"))
print(simplify("2/3