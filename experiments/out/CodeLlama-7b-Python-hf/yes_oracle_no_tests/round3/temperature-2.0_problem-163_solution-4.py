def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: i
	Do not include these tokens in the code: num
	"""



    if a > b:
        a, b = b, a
    else:
        a = a
        b = b

    # Write your code here.
    if a % 2 == 0:
        a += 2
    else:
        a += 1

    result = []
    for number in range(a, b+1, 2):
        result.append(number)

    return result






































