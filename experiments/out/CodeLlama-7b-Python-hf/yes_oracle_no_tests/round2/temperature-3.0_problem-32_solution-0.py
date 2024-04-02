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
    if len(xs) % 2 != 0 or max(xs) == 0:
        return None
    return -xs[1] / (xs[0] + 2 * xs[2])


def main():
    import doctest

    doctest.testmod()
    print("[WARNING]: This code is untested on the system and may contain errors.")
    print("[WARNING]: Code contains tokens that will not be accepted.")
    print("[WARNING]: Code contains tokens that are not included in the code.")

    xs = [1, 2, 3, 4]
    print(f"poly({xs}, 2) = {poly(xs, 2)}")
    print(f"find_zero({xs}) = {find_zero(xs)}")


if __name__ == "__main__":
    main()
