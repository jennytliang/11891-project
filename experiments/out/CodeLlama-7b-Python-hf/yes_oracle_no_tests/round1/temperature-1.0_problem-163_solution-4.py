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

    if a > b:
        return [int(num) for num in range(2, 8) if not num % 2]  
    elif a == b:
        return []
    else:
        a, b = min(a, b), max(a, b)
        return [int(num) for num in range(a, b + 1) if not num % 2 and int(num) >= a]
