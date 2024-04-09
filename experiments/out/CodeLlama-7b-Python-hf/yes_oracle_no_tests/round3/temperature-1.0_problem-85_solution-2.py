def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: #
	"""
    return sum([lst[i] for i in range(len(lst)) if i % 2 != 0])




def remove(lst):
    """Given a list of integers lst, remove the integers that are in even indices.


    Examples:
        remove([4, 2, 6, 7]) ==> [2, 7]
    
	Do not include these tokens in the code: #
	"""
    return [lst[i] for i in range(len(lst)) if i % 2 == 0]




def reverse(lst):
    """Given a list of integers lst, reverse the list.


    Examples:
        reverse([4, 2, 6, 7]) ==> [7, 6, 2, 4]
    
	Do not include these tokens in the code: #
	"""
    return lst[::-1]




def reverse_every_k(lst, k):
    """Given a list of integers lst and a positive integer k. reverse every k elements in the list.


    Examples:
        reverse_every_k([4, 2, 6, 7], 2) ==> [2, 6, 4, 7]
        reverse_every_k([4, 2, 6, 7], 4) ==> [4, 2, 6, 7]
    
	Do not include these tokens in the code: #
	"""
    return [lst[i] for i in range(len(lst))]




def is_sorted(lst):
    """Given a list of integers lst. return whether the list is sorted in an ascending order or not.


    Examples:
        is_sorted([4, 2, 6, 7]) ==> False
        is_sorted([2, 4, 6, 7]) ==> True
    
	Do not include these tokens in the code: #
	"""
    return lst == sorted(lst)




def sort(lst):
    """Given a list of integers lst. sort the