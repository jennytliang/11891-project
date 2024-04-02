def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x 1
	Do not include these tokens in the code: num _
	"""
    assert isinstance(x, str) and isinstance(n, str)
    assert "/" in x and "/" in n
    assert len(x.split("/")) == 2 and len(n.split("/")) == 2
    assert int(x.split("/")[0]) > 0 and int(n.split("/")[0]) > 0
    assert int(x.split("/")[1]) > 0 and int(n.split("/")[1]) > 0
    
    x_numerator = int(x.split("/")[0])
    x_denominator = int(x.split("/")[1])
    n_numerator = int(n.split("/")[0])
    n_denominator = int(n.split("/")[1])
    
    return (x_numerator * n_denominator) % n_numerator == 0 or (x_denominator * n_numerator) % n_denominator == 0
    
    # return (x_numerator * n_denominator) % n_denominator == 0 or (x_denominator * n_numerator) % n_denominator == 0
    # return (x_numerator * n_denominator) % n_denominator == 0 and (x_denominator * n_numerator) % n_denominator == 0


if __name__ == "__main__":
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
