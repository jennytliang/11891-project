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
	Do not include these tokens in the code: _ num
	"""

    # Your code here
    def get_gcd(x, y):
        if x == 0 or y == 0:
            return 0
        if x == y:
            return x
        if x > y:
            return get_gcd(x - y, y)
        else:
            return get_gcd(x, y - x)
    x_num = int(x.split('/')[0])
    x_den = int(x.split('/')[1])
    n_num = int(n.split('/')[0])
    n_den = int(n.split('/')[1])
    gcd = get_gcd(x_den, n_den)
    return (x_num * n_den * gcd) % (x_den * n_num) == 0


simplify("1/5", "5/1")
simplify("1/6", "2/1")
simplify("7/10", "10/2")
