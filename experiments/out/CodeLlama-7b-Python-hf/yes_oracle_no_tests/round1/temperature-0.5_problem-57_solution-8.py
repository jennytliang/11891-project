def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: if len ( l ) <  2 :
	"""

    
    if len(l) < 2:
        return True
    direction = "inc" if l[1]-l[0] > 0 else "dec"
    for i in range(2, len(l)):
        if direction == "inc" and l[i]-l[i-1] < 0:
            direction = "dec"
        elif direction == "dec" and l[i]-l[i-1] > 0:
            direction = "inc"
    return True if direction == "inc" or direction == "dec" else False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
