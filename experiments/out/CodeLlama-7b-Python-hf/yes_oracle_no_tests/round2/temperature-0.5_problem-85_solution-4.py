def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0])

if __name__ == '__main__':
    print("Example:")
    print(add([4, 2, 6, 7]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert add([4, 2, 6, 7]) == 2
    assert add([34, 13, 7, 3, 2]) == 13
    assert add([34, 13, 7, 3]) == 13
    assert add([34, 13, 7]) == 13
    assert add([34, 13]) == 13
    assert add([34]) == 0
    assert add([]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
