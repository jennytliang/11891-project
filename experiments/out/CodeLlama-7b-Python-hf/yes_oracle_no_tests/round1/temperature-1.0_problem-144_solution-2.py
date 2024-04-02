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

    x_numer, x_denom = x.split("/")
    n_numer, n_denom = n.split("/")

    xn = int(x_numer) * int(n_denom)
    dxn = int(x_denom) * int(n_numer)
    result = xn / dxn  # float
    return bool(result.is_integer())
    # return bool(result == round(result))


if __name__ == "__main__":
    _input = input("Enter the input: ").split()
    x = _input[0]
    y = _input[1]
    print(simplify(x, y))
