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
        a, b = b, a
    return [x for x in range(a, b+1) if x % 2 == 0]


if __name__ == '__main__':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print(generate_integers(a, b))
