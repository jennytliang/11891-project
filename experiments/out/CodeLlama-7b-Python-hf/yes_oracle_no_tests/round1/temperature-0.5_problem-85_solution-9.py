def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 0
    for i in range(0, len(lst), 2):
        r += lst[i]
    return r


def main():
    print('The sum of even elements at odd indices is: ' + str(add([4, 2, 6, 7])))


if __name__ == "__main__":
    main()
