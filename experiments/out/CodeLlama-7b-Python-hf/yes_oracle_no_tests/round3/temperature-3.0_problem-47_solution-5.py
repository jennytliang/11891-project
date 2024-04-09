def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Do not include these tokens in the code: sorted _
	"""


    sorted_l = sorted(l)
    i = len(l)//2
    return l[i]



def mode(l: list):
    """Return mode of elements in the list l.
    >>> mode([1, 1, 2, 3, 3, 3, 3, 4, 5])
    3
    >>> mode([1, 2, 2, 3, 4])
    [2, 3]
    
	Do not include these tokens in the code: sorted _
    """


    sorted_l = sorted(l)
    i = 1
    while i < len(l):
        if sorted_l[i] == sorted_l[i-1]:
            i += 1
        else:
            return sorted_l[i-1]
    return None



def standard_deviation(l: list):
    """Return standard deviation of elements in the list l.
    >>> standard_deviation([3, 1, 2, 4, 5])
    1.5811388300841898
    >>> standard_deviation([-10, 4, 6, 1000, 10, 20])
    1017.2192801689453
    
	Do not include these tokens in the code: sorted _
    """


    sorted_l = sorted(l)
    sum = 0
    for i in range(len(l)):
        sum += (sorted_l[i] - mean(l))**2
    return (sum/len(l))**0.5



def mean(l: list):
    """Return mean of elements in the list l.
    >>> mean([3, 1, 2, 4, 5])
    3.0
    >>> mean([-10, 4, 6, 1000, 10, 20])
    361.66666666666666
    
	Do not include these tokens in the code: sorted _
    """