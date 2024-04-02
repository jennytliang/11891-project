def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: if a > b : a , b = b
	"""
    # code goes here

    if a>b:
        a,b=b,a

    final =(int(a/2)*2)
    temp=final
    finals=list()
    while (final<b):
        final += 2
        finals.append(round(final))
        
    print(finals)
    return finals


if __name__ == '__main__':
    print("Example:")
    print(generate_integers(2, 8))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == [2]
    print("Coding complete? Click 'Check' to earn cool rewards!")