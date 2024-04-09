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
    
	Include these tokens in the code: d xs = [ xs [ i ]
	Do not include these tokens in the code: return sum ([ co eff
	"""
    assert len(xs) % 2 == 0
    assert max(xs) != 0
    return - (xs[1] / xs[0])


# === Measures ===


def measure_distance_from_origin(x: float):
    """
    measure_distance_from_origin measures the distance
    from the origin to the point (x, 0).
    """
    return math.fabs(x)


def measure_distance_between_two_points(x1: float, x2: float):
    """
    measure_distance_between_two_points measures the distance
    between two points (x1, 0) and (x2, 0).
    """
    return math.fabs(x1 - x2)


def measure_distance_between_two_polygons(xs: list, ys: list):
    """
    measure_distance_between_two_polygons measures the distance
    between two polygons (xs, 0) and (ys, 0).
    """
    return measure_distance_between_two_points(xs[-1], ys[-1])


# === Visualizations ===


def visualize_polygon(xs: list, ys: list):
    """
    visualize_polygon draws a polygon on the screen.
    """
    print(f"xs: {xs}")
    print(f"ys: {ys}")


def visualize_polygon_with_text(xs: list, ys: list, text: str):
    """
    visualize_polygon_with_text draws a polygon on the screen
    and also prints out the text.
    """
    print(f"xs: {xs}")
    print(f"ys: {ys}")
    print(f"text: {text}")


# === Main ===


def main():
    """
    The main function is used for testing your code.
    Once you write all the functions above, you can try running the
    main function to see if your code works correctly.
    Once it works, you should be able to generate your