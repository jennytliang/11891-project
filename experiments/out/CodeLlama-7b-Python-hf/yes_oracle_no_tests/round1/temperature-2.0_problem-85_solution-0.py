def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            s += str(lst[i]) + " "
    return s


def add_2(lst):
    return " ".join(str(lst[i]) for i in range(len(lst)) if i % 2 == 1)


def add_3(lst):
    return " ".join(lst[i] for i in range(len(lst)) if i % 2 == 1)


def add_4(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_5(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_6(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_7(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_8(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_9(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_10(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_11(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_12(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_13(lst):
    return " ".join(lst[i] for i in range(1, len(lst), 2))


def add_14(lst):
    return " ".join(lst[i] for