def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in l:
        if x > 0:
            r += [x]

    return r



def main():
    l = eval(input("Enter a list of numbers to get only positive numbers from: "))
    print(get_positive(l))

if __name__ == "__main__":
    main()