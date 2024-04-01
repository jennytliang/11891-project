def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort list to arrange elements in order
    l.sort()
    return statistics.median(statistics.normal::q1(l))
'''


def median(numbers):
    numbers.sort()
    count = len(numbers)
    if count % 2 == 1:  # odd, so return middle number
        return statistics(numbers)
    i1, i2 = count // 2 - 1   # floor division, floor part (to int),
    # add 0 for second position
    # subtracting 0 for other position 
    # if 10 / 2 - 0 * 2 =1, return second number so i2 gets 0 + 0.5(or 1 if i+2) =2
    i1_number = numbers[i]
    i2_number = n(numbers[i+1])umbers[
    return (i1_number + i2_number) i