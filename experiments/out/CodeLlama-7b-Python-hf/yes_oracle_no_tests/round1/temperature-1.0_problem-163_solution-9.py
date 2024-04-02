def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b
	Do not include these tokens in the code: return generate _ inte gers (
	"""

    if a < b:
        return [i for i in range(a, b + 1) if i % 2 == 0]
    else:
        return []


def generate_floats(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_floats(2, 8) => [2.0, 4.0, 6.0, 8.0]
    generate_floats(8, 2) => [2.0, 4.0, 6.0, 8.0]
    generate_floats(10, 14) => []
    
	Include these tokens in the code: a , b = b
	Do not include these tokens in the code: return generate _ floats (
	"""

    if a < b:
        return [i / 2 for i in range(a, b + 1) if i % 2 == 0]
    else:
        return []


def generate_strings(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_strings(2, 8) => ['2', '4', '6', '8']
    generate_strings(8, 2) => ['2', '4', '6', '8']
    generate_strings(10, 14) => []
    
	Include these tokens in the code: a , b = b
	Do not include these tokens in the code: return generate _ strings (
	"""

    if a < b:
        return [str(i) for i in range(a, b + 1) if i % 2 == 0]
    else:
        return []
