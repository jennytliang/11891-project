import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    
	Include these tokens in the code: d
	Do not include these tokens in the code: return sum ([ co eff * math
	"""
    a = xs[0]
    b = xs[1]
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # 11
    # 12
    # 13
    # 14
    # 15
    # 16
    # 17
    # 18
    # 19
    # 20
    # 21
    # 22
    # 23
    # 24
    # 25
    # 26
    # 27
    # 28
    # 29
    # 30
    # 31
    # 32
    # 33
    # 34
    # 35
    # 36
    # 37
    # 38
    # 39
    # 40
    # 41
    # 42
    # 43
    # 44
    # 45
    # 46
    # 47
    # 48
    # 49
    # 50
    # 51
    # 52
    # 53
    # 54
    # 55
    # 56
    # 57
    # 58
    # 59
    # 60
    # 61
    # 62
    # 63
    # 64
    # 65
    # 66
    # 67
    # 68
    # 69
    # 70
    # 71
    # 72
    # 73
    # 74
    # 75
    # 76
    # 77
    # 78
    # 79
    # 80
    # 81
    # 82
    # 83
