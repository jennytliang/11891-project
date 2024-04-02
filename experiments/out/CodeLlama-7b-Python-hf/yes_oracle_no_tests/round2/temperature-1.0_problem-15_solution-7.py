def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map (
	Do not include these tokens in the code: r tn _ string = ''
	"""
    return ' ' . join ( map ( str , range ( n + 1 ) ) )

    #############################
    # Warm up 
    print('\n'.join(string_sequence(n)))
    print('\n'.join(string_sequence(2)))
    print('\n'.join(string_sequence(5)))
    print(string_sequence(5))

    #############################
    # Coding
    # return ''.join(map(str, list(range(n+1))))
    
    # for i in range(n+1):
    #     print('', i)
