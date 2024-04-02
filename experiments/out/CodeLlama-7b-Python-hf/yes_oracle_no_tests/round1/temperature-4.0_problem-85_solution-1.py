def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    # s = lst[0]
    # for i in range(1, len(lst), 2):
    #     s += lst[i]
    # return s

    # s = lst[0]
    # for i in range(1, len(lst), 2):
    #     s += lst[i]
    # return s

    s = lst[0]
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s


def main():
    print('----------')
    print(add([4, 2, 6, 7]))
    print('----------')
    print(add([4, 0, 6, 7]))
    print('----------')
    print(add([4, 0, 2, 6, 7]))
    print('----------')


if __name__ == '__main__':
    main()
