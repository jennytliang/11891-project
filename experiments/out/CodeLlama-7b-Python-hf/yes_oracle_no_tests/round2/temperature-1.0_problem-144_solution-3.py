def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Do not include these tokens in the code: # TO DO : Write your
	"""
    num_exp = int(x.split('/')[0])
    den_exp = int(x.split('/')[1])
    num = int(n.split('/')[0])
    den = int(n.split('/')[1])

    mul_exp = num*num_exp
    div_exp = den*(num_exp//den)
    rem = mul_exp - div_exp

    return bool(rem)

    # if num * num_exp > den * div_exp:
    #     return 'true'
    # else:
    #     return 'false'

if __name__ == "__main__":
    x, n = input(), input()
    print(simplify(x, n))
