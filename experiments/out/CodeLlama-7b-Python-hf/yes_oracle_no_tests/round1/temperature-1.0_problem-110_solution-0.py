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
    
	Include these tokens in the code: c nt _ odd =
	Do not include these tokens in the code: if
	"""
    lst1 = [int(c) for c in lst1]
    lst2 = [int(c) for c in lst2]
    #your code here
    lst1_even = []
    lst2_even = []
    for l in lst1: 
        if l % 2 == 0:
            lst1_even.append(l)
    
    for l in lst2:
        if l % 2 == 0:
            lst2_even.append(l)
            
    if len(lst1_even) != 0 and len(lst2_even) != 0:
        lst1_odd = [x for x in lst1 if x not in lst1_even]
        lst2_odd = [x for x in lst2 if x not in lst2_even]
            

        while len(lst1_odd) > 0 and len(lst2_odd) > 0:

            if lst1_odd[0] + lst2_odd[0] % 2 != 0:
                lst1_odd.pop(0)
                lst2_odd.pop(0)
            elif len(lst1_odd) == 0 or len(lst2_odd) == 0:
                no = True
            else:
                lst1_odd_e = lst2[0]
                lst2_odd_e = lst1[0]
                lst1_odd.pop(0)
                lst2_odd.pop(0)
                lst1_odd.append(lst1_odd_e)
                lst2_odd.append(lst2_odd_e)
        
    else: 
        return "NO"

    lst1_remaining = []
    lst2_remaining = []
    for l in lst1:
        if l % 2 != 0:
            lst1_remaining.append(l)
    for l in lst2:
        if l % 2 != 0:
            lst2_remaining.append(l)
    
            

    if len(lst1_remaining) == 0 and len(lst2_