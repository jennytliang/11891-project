def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if n == 1:
        return x == n
    # edge case

    if x > n:
        tmp = 2
        while n < x:
            tmp *= tmp
    else:

    # loop over power of 2, each power should result in a lesser number than n
        # once we get to x - n we stop
            tmp = 2
            print("tmp", tmp)
    return x == (n**int)

