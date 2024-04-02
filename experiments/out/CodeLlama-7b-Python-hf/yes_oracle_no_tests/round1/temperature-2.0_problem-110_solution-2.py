def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    
	Include these tokens in the code: c nt _ odd = len ( list ( filter
	"""
    #hint: 
    # 1. Check if all elements in lst1 are odd or not
    # 2. if yes, return "NO"
    # 3. else, create a new list with all the elements of lst1
    # 4. check if lst2 contains all the elements of lst1
    # 5. if yes, return "YES"
    # 6. else, return "NO"
    
    #input validation
    if not lst1 or not lst2:
        return "NO"
    
    #check if lst1 is all odd
    if all(elem%2 != 0 for elem in lst1):
        return "NO"
    
    #create a new list with all the elements of lst1
    lst1_new = lst1.copy()
    
    #check if lst2 contains all the elements of lst1
    if all(elem in lst2 for elem in lst1_new):
        return "YES"
    else:
        return "NO"
    
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    #input validation
    if not lst1 or not lst2:
        return "NO"
    
    #check if lst1 is all odd
    if all(elem%2 != 0 for elem in lst1):
        return "NO"
    