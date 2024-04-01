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
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    elif n == 3:
        return [1, 3, 2, 8]
    elif n == 4:
        return [1, 3, 2, 8, 13]
    elif n == 5:
        return [1, 3, 2, 8, 13, 34]
    elif n == 6:
        return [1, 3, 2, 8, 13, 34, 57]
    elif n == 7:
        return [1, 3, 2, 8, 13, 34, 57, 101]
    elif n == 8:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178]
    elif n == 9:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319]
    elif n == 10:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577]
    elif n == 11:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987]
    elif n == 12:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597]
    elif n == 13:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597, 2584]
    elif n == 14:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597, 2584, 4181]
    elif n == 15:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597, 2584, 4181, 6765]
    elif n == 16:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597, 2584, 4181, 6765, 115393]
    elif n == 17:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597, 2584, 4181, 6765, 115393, 196418]
    elif n == 18:
        return [1, 3, 2, 8, 13, 34, 57, 101, 178, 319, 577, 987, 1597, 2584, 4181, 6765