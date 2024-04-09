def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: # base case
	"""
    if a > b:
        return generate_integers(b, a)
    elif a % 2 != 0:
        a += 1
    elif b % 2 != 0:
        b -= 1
    if a > b:
        return []
    elif a == b:
        return [a]
    else:
        return [a] + generate_integers(a + 2, b)
    

def test_function(test_case):
    test_input, test_expected = test_case
    actual = generate_integers(test_input[0], test_input[1])
    if actual == test_expected:
        print("Pass")
    else:
        print("Fail")

test_function(((2, 8), [2, 4, 6, 8]))
test_function(((8, 2), [2, 4, 6, 8]))
test_function(((10, 14), []))
test_function(((10, 16), [12, 14, 16]))
test_function(((10, 15), [12, 14]))
test_function(((10, 17), [12, 14, 16]))
test_function(((12, 16), [12, 14, 16]))
test_function(((12, 17), [12, 14, 16]))
test_function(((12, 18), [12, 14, 16, 18]))
test_function(((0, 10), [2, 4, 6, 8, 10]))
test_function(((10, 100), [2, 4, 6, 8, 10]))
test_function(((100, 1000), [2, 4, 6, 8, 10]))
test_function(((1000, 10000), [2, 4, 6,