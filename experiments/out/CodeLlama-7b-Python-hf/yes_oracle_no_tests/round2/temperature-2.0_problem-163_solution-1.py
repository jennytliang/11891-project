def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b , a
	"""


    if 10 < a or a > 99 or 10 < b or b > 99:
        print("a and b must be between 10 and 99")
        return

    if a > b:
        a, b = b, a

    generated_integers = []
    while a <= b:
        a_str = str(a)
        if int(a_str[0]) % 2 == 0 and int(a_str[1]) % 2 == 0:
            generated_integers.append(a)
        a += 1
    return generated_integers


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
