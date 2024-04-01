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
    """
    # TODO 12/01: find zero, remove duplication.
    y_list = []
    for x in range(0, xs[-1] + 10):
        y_list.append(poly(xs, x))
    return y_list.index(0)


if __name__ == "__main__":
    # import doctest
    xs = [5, 4, 3, 2, 0]    # x^4
    assert round(find_zero([5, -4, 3, -2, 0.0]), 2) == -1
    # import pdb; pdb.set_trace()
    n = math.ceil(-2 * math.log10(abs(poly(xs, x=1))))
    assert round(2**(-n * n + n + 1), 0) == 16

    # 0에 달줄 알고 실험한 거.
    # print(round(find_zeros(xs), 2), n)
    # print(round(math.pow(2, -n*n + n +1) ,2)
    # print(4**5 // 5)