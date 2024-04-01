def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: ( list
	"""


    return 



def main():
    l1 = [1, 4, 3, 34, 653, 2, 5]
    l2 = [5, 7, 1, 5, 9, 653, 121]
    print(f"Common elements between {l1} and {l2} are {common(l1, l2)}")
    l1 = [5, 3, 2, 8]
    l2 = [3, 2]
    print(f"Common elements between {l1} and {l2} are {common(l1, l2)}")


if __name__ == '__main__':
    main()
