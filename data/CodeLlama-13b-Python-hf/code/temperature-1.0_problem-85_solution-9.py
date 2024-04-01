def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return 0
    else:
        if lst[0] % 2 == 0:
            return lst[0] + add(lst[2:])
        else:
            return add(lst[1:])

print(add([4, 2, 6, 7]))

