def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
	Include these tokens in the code: if n ==
	"""
    # your code here
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        n1, n2, n3 = 1, 3, 2
        result = [n1, n2, n3]
        for i in range(n - 2):
            n1, n2, n3 = n2, n3, n1 + n2 + n3
            result.append(n1)
        return result


if __name__ == '__main__':
    print("Example:")
    print(tri(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(tri(0)) == [1]
    assert list(tri(1)) == [1, 3]
    assert list(tri(2)) == [1, 3, 2]
    assert list(tri(3)) == [1, 3, 2, 8]
    assert list(tri(4)) == [1, 3, 2, 8, 11]
    assert list(tri(5)) == [1, 3, 2, 8, 11, 23]
    print("Coding complete? Click 'Check' to earn cool rewards!")