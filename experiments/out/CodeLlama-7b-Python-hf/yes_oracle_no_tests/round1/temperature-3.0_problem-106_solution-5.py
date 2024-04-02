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
    return []


def check(candidate):

    # Check some simple cases
    assert candidate(1) == [1], "First test error"
    assert candidate(2) == [1, 2], "Second test error"
    assert candidate(3) == [1, 2, 6], "Third test error"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(5) == [1, 2, 6, 24, 15], "Fourth test error"

if __name__ == "__main__":
    check(f)
