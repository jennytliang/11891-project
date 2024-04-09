def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec
	Do not include these tokens in the code: # Y OUR CO DE
	"""
    # YOUR CODE HERE
    # inc = 0
    # dec = 0
    # for i in range(len(l)-1):
    #     if l[i] < l[i+1]:
    #         inc += 1
    #     elif l[i] > l[i+1]:
    #         dec += 1
    #     else:
    #         return False
    # if inc == len(l)-1 or dec == len(l)-1:
    #     return True
    # else:
    #     return False
    # if inc == len(l)-1:
    #     return True
    # elif dec == len(l)-1:
    #     return True
    # else:
    #     return False
    # if inc > 0 and dec == 0:
    #     return True
    # elif dec > 0 and inc == 0:
    #     return True
    # else:
    #     return False
    if l == sorted(l):
        return True
    elif l == sorted(l, reverse=True):
        return True
    else:
        return False