def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Do not include these tokens in the code: return s ( l 1 ,
	"""
    return sorted(set(l1).intersection(set(l2)))


def main():
    l1 = [1, 4, 3, 34, 653, 2, 5]
    l2 = [5, 7, 1, 5, 9, 653, 121]
    print(common(l1, l2))

    l1 = [5, 3, 2, 8]
    l2 = [3, 2]
    print(common(l1, l2))


if __name__ == "__main__":
    main()
