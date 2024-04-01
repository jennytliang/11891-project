def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if l1 and l2 and (len(l1) != 0 and len(l2) != 0):
        l3 = list(set("".join([i+""for j in [list(set(i))] for i in [[item] for item in (list((set(j).intersection(set(l2)))))*2]])).join("").split(""))
    else: l3 = []
    return l3

if __name__=="__main__":
    print("here")