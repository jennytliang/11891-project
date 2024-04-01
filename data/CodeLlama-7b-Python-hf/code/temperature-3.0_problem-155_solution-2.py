def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    result = [0, 0]
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            result[0] += 1
        else:
            result[1] += 1
    return tuple(result)


def test_even_odd():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(0) == (0, 1)
    assert even_odd_count(10) == (1, 1)
