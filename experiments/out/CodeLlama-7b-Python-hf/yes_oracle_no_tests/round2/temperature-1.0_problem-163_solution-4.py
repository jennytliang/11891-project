def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: return [ int ( num ) for num
	"""


    if 0 <= a < 100 and 0 <= b < 100:
     return [num for num in range(a, b + 1) if num % 2 == 0]

