def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l.sort()
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            l.pop(i+1)
        else:
            i += 1
    return l


def main():
    s = int(input())
    l = list(map(int, input().split()))
    l = unique(l)
    print(l[-1])


