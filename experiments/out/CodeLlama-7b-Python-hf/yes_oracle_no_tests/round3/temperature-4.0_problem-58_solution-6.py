def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: return sorted ( list ( set
	Do not include these tokens in the code: s 1 =
	"""
    return sorted(list(set(l1) & set(l2)))


def main():
    """Read command-line arguments and convert them.
    >>> main()
    """
    import sys
    args = sys.argv[1:]
    assert len(args) == 2, "Please provide two lists to compare."
    l1 = args[0].split(",")
    l2 = args[1].split(",")
    result = common(l1, l2)
    print(result)


if __name__ == "__main__":
    main()
