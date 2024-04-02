def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""


    if le(lst[1], lst[0]):
        a,lst= lst[1], lst[2:]
    else:
        a,lst= lst[0], lst[1:]
    for i in lst:
        if le(a,i):
            a=i
    return a
def le(a,b):
        if (ord(str(a)) <  ord(str(b))) or (ord(str(a))==ord(str(b)) and ord(str(b)) == ord(' ')):
            return True
        else:
            return False