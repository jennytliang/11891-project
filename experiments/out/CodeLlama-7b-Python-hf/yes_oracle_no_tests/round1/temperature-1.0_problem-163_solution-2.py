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

    if a>b or b<a:
        return []
    elif b-a==0:
        return [a]
    # Write at least one line of code below:
   
    even = []
    for i in range(a,b+1):
        str_a = str(i)
        if '0' == str_a[-1] or '2' == str_a[-1] or '4' == str_a[-1] or '6' == str_a[-1] or '8' == str_a[-1]:
            even.append(i)
    
    # Write at least one line of code below:
    return even

    pass

if __name__ == '__main__':
    print(generate_integers(2, 8))
    print(generate_integers(8, 2))
    print(generate_integers(10, 14))
