def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 1 and lst[i] % 2 == 0])



print(add([4, 2, 6, 7]))
print(add([4, 2, 6, 7, 8]))
print(add([4, 2, 6, 7, 8, 10]))
print(add([4, 2, 6, 7, 8, 10, 11]))
print(add([4, 2, 6, 7, 8, 10, 11, 12]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13, 14]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13, 14, 15]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
print(add([4, 2, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
print(add([4, 2, 6, 7