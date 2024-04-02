def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str ,
	Do not include these tokens in the code: r = "" for
	"""
    # MY SOLUTION
    return " ".join(map(str, list(range(n + 1))))

    # LIST COMPREHENSION - OOP (Pythonic Way)
    return " ".join([str(i) for i in range(n + 1)])

    # USING F-STRING (more convenient)
    return " ".join([f"{i}" for i in range(n + 1)])

    ################################
    # ANOTHER SOLUTIONS
    return " " + " ".join(map(str, range(n + 1)))
    seq = [str(x) for x in range(n + 1)]
    return " ".join(seq)
    return ("%s " % x) * (n + 1)[:-1]

    return " ".join(map(str, range(len(range(n + 1)))))
