def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even = 0
    for index in range(1, len(lst), 2):
        even += lst[index]
    return even


def add_naive(lst):
    if lst == None or len(lst) == 0:
        return None

    even_sum = 0
    for index in range(len(lst)):
        if index%2 == 0:
            even_sum += lst[index]

