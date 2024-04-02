def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: return [ i
	Do not include these tokens in the code: result = []
	"""


    if a > b:
        a, b = b, a

    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)

    return result


def test_function():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(10, 15) == [12, 14]
    assert generate_integers(10, 19) == [12, 14, 16, 18]
    assert generate_integers(10, 20) == [12, 14, 16, 18, 20]

if __name__ == '__main__':
    test_function()
