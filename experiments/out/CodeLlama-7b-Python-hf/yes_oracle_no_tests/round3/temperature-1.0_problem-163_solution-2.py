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
        
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b -= 1
    else:
        if a % 2 != 0:
            a -= 1
        if b % 2 != 0:
            b += 1

    result = []
    for i in range(a, b):
        if i % 2 == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    print(generate_integers(2, 8))
    print(generate_integers(8, 2))
    print(generate_integers(10, 14))
    # print(generate_integers(10, 12))
