def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s= 0
    for i in range(len(lst)):
        if (i%2==1 and lst[i] % 2!=0):
            s+= lst[i]
    return s

add([4, 2, 6, 7]) #== 2
#=======================

def delete(lst):
    """Delete the even numbers from lst and return the new list.


    Examples:
        delete([1, 2, 3, 1]) ==> [1, 3, 1]
    
	Include these tokens in the code: new_lst =
	"""
    new_lst = []
    for i in lst:
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst

delete([1, 2, 3, 1]) #== [1, 3, 1]
#=======================


def reverse(lst):
    """Given a list lst, reverse the list in place. That is, we want to change the items in lst so they appear in the opposite order they currently do.

    Examples:
        reverse([1, 2, 3, 4, 5]) ==> [5, 4, 3, 2, 1]
    
	Include these tokens in the code:
    """
    lst = lst.reverse()
    lst.reverse()
    return lst
    
reverse([1, 2, 3, 4, 5]) #== [5, 4, 3, 2, 1]
#=======================


def reverse_inverse(lst):
    """Given a list of integers, create a new list with the same integers in reverse order, but also keep the integers the same way

    Examples:
        reverse_inverse([1, 2, 3, 4, 5]) ==> [5, 1, 2, 3, 4]
    
	Include these tokens in the code: inverse = reverse(lst) + lst
	"""
    inverse = reverse(lst) + lst
    return inverse

reverse_