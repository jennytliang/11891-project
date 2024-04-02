def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str , range
	"""
    return " ".join(map(str, range(n+1)))
    # Your code here


if __name__ == "__main__":
    print("OK" if (string_sequence(0) == "0") else "RETRY")
    print("OK" if (string_sequence(2) == "0 1 2") else "RETRY")
    print("OK" if (string_sequence(3) == "0 1 2 3") else "RETRY")
