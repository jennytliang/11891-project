def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""

    s = ""        # to hold string representation of sum
    for i,item in enumerate(lst):
        if i % 2 == 1 and item % 2 == 0:
            s += str(item)
    return s


print("4 2 6 7")
print(add([4, 2, 6, 7]))

print("4 7 8 9")
print(add([4, 7, 8, 9]))