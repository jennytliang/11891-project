def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc
	Do not include these tokens in the code: # sort list into asc ending order
	"""
    # sort list into ascending order
    l.sort()
    
    # create a variable to store the previous value
    prev_val = l[0]
    
    # create a variable to store the status of the list
    inc = True
    
    # loop through the list
    for val in l:
        # if the current value is not greater than the previous value
        if val <= prev_val:
            # set the inc variable to False
            inc = False
            # break out of the loop
            break
        # otherwise
        else:
            # set the prev_val variable to the current value
            prev_val = val
            
    # return the inc variable
    return inc


def main():
    import doctest
    doctest.testmod()
    l = [1, 2, 4, 20]
    print(monotonic(l))

if __name__ == "__main__":
    main()
