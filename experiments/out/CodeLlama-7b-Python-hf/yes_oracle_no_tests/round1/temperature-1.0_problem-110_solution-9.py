def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    
	Include these tokens in the code: c nt _ odd =
	Do not include these tokens in the code: if
	"""

    if(lst1 != []):
        if(lst2 != []):
            if len(lst2) > len(lst1):
                return "NO"
            elif(lst1[0] % 2 == 0):
                return "YES"
            elif(lst2[0] % 2 == 0):
                return (exchange(lst2[1:],lst1))
            else:
                return "NO"




def exchange0(lst1, lst2):
    """Solution to the exchange problem using Python 3.0+ features.

    >>> exchange([3, 4, 5], [1, 2])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 3, 5])
    'NO'
    """
    return "YES" if all(x%2==0 for x in lst1+lst2) else "NO"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
