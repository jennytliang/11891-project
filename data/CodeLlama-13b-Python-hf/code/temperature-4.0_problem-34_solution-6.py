def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    u_list = list(dict(Counter(l)).keys())
    sort_u_list = sorted(u_list, key= lambda el: (el.__hash__(), str(el))) # To ensure 0 is before False
    return sort_u_list
# end def