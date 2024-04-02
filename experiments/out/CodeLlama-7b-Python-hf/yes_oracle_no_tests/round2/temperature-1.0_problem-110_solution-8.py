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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: total
	"""
    def is_not_contain_odd(lst):
    	not_contain_odd = True
    	for i in lst:
    		if i % 2 == 1:
    			not_contain_odd = False
    	return not_contain_odd

    lstnub = [] # new list for getting rid of similar elements between lst1 and lst2
    for i in lst1:
    	if i not in lstnub:
    		lstnub.append(i)

    for j in lst2:
    	if j not in lstnub:
    		lstnub.append(j)

    # lstnub get the list made of unique elements of lst1 and lst2

    if is_not_contain_odd(lstnub):
    	return "YES"

    else:
    	return "NO"

print exchange([1, 2, 3, 4], [1, 2, 3, 4])
print exchange([1, 2, 3, 4], [1, 5, 3, 4])