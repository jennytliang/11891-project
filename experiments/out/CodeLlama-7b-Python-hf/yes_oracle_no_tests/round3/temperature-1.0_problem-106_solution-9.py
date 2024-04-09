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
    return [None for i in range(n)]


def main():
    print(f(5))
    print(f(0))
    print(f(1))
    print(f(2))
    print(f(3))
    print(f(4))
    print(f(5))
    print(f(6))
    print(f(7))
    print(f(8))
    print(f(9))
    print(f(10))


if __name__ == '__main__':
    main()
