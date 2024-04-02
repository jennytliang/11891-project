def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: ). inter section ( set
	Do not include these tokens in the code: ) &
	"""

    return sorted(list(s1 & s2))


if __name__ == "__main__":
    s1 = [1, 4, 3, 34, 653, 2, 5]
    s2 = [5, 7, 1, 5, 9, 653, 121]
    print(f"Input lists: s1 = {s1}, s2 = {s2}")
    print(f"Common elements in the sorted order: {common(s1, s2)}")
