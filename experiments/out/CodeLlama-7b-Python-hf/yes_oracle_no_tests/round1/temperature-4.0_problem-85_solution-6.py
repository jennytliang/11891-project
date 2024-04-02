def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = 0
    for i in range(0, len(lst), 2):
        if i % 2 == 0:
            s += lst[i]
    return s


def main():
    print(add([4, 2, 6, 7]))
    print(add([3, 2, 4, 5, 6, 7]))
    print(add([3, 3, 3, 3, 3, 3]))


if __name__ == "__main__":
    main()
