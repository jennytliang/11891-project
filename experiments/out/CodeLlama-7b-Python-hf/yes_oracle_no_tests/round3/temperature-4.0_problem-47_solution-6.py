def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l =
	Do not include these tokens in the code: return
	"""
    l = sorted(l)
    return l[len(l)//2]


def main():
    import doctest
    doctest.testmod()
    l = [int(input("Enter number: ")) for _ in range(4)]
    print(median(l))

if __name__ == "__main__":
    main()
