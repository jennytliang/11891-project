def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(map(lambda x: is_one_ends(str(n)[0] * x), range(1, 10)))

def is_ones(n):
    return n == int('1111111111')

def is_one_ends(n):
    return n == int('1' + '1' * 10)

def starts_one_or_end_one(n):    
    total = (10, 2 ** 10)
    start = [1] + range(1, 10)
    end = [int(str() + (x + 1) * '1') for x in start]
    for s in start:
        for n in range(10):
            total += start_one_ends[s][n]
    print start, end
