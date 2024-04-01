def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            s += lst[i]
    return s


# tests
def run_test():
    print(add([4, 2, 6, 7]))  # 2
    print(add([1, 3, 5, 7]))  # 0
    print(add([1, 2, 3, 4]))  # 0
    print(add([1, 2, 3, 4, 5]))  # 3


def main():
    run_test()


if __name__ == "__main__":
    main()