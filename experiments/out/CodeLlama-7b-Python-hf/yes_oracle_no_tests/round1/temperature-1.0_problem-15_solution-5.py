def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r=str(0)
    for s in range (1,n+1):
        r = r +" "+str(s)
    return r 
    # ...

if __name__=='__main__':
    a=string_sequence(8)
    print(a)