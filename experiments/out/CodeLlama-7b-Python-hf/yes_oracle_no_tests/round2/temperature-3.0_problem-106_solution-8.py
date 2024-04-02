def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
	Include these tokens in the code: if n ==
	"""
    return n


def check(candidate):

    # Check some simple cases
    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(3) == [1, 2, 6]
    assert candidate(4) == [1, 2, 6, 24]
    assert candidate(2) == [1, 2]
    assert candidate(1) == [1]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(10) == [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


if __name__ == "__main__":
    check(f)
