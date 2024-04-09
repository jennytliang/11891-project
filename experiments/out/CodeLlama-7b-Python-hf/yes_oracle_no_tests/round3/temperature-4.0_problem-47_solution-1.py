def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l =
	Do not include these tokens in the code: return
	"""
    l=sorted(l)
    return l[(len(l))//2]
    
def median2(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l =
	Do not include these tokens in the code: return
	"""
    l=sorted(l)
    if len(l)==0:
        return None
    elif len(l)%2==0:
        return (l[(len(l))//2]+l[(len(l))//2-1])/2
    else:
        return l[(len(l))//2]

def main():
    import doctest
    doctest.testmod()
    print("Example:")
    print(median([3, 1, 2, 4, 5]))
    print(median([-10, 4, 6, 1000, 10, 20]))

if __name__ == "__main__":
    main()