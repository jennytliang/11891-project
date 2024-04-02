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
    # WRITE YOUR CODE HERE
    return n


if __name__ == '__main__':
    print("Example:")
    print(f(5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 6]
    assert f(1) == [1]
    assert f(0) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")