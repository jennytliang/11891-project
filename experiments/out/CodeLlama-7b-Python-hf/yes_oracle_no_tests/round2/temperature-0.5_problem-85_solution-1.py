def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    #pass
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    return sum


print(add([4, 2, 6, 7]))
print(add([4, 2, 6, 7, 1]))
print(add([4, 2, 6, 7, 1, 3]))
print(add([4, 2, 6, 7, 1, 3, 5]))
print(add([4, 2, 6, 7, 1, 3, 5, 8]))
print(add([]))
print(add([1]))
print(add([1,2]))

