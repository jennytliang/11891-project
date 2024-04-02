def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: l 2
	"""
    l2 = []
    for i in range(len(l)):
        if i%2 == 1: 
            l2.append(l[i]) 
    l2 = sorted(l2)
    for j in range(len(l2)): 
        l[j*2] = l2[j]
    return l

#### DO NOT MODIFY ANYTHING ABOVE ####
####  YOUR CODE GOES BELOW HERE  ####

sort_even([1, 45, 31, 9, 87, 23, 76])    
l = [4, 5, 6]
sort_even(l)  

sample = [1, 45, -10, 4, 0, 123, -4, 91]
sort_even(sample)
