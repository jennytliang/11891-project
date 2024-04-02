def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [
	Do not include these tokens in the code: ## BEGIN S OL UT ION
	"""
    if len(l) == 0:
        return l
    even = l[1::2] # create new list from l starting at 1st odd index and having every second index
    even.sort() # sort even list
    # construct l'
    l_prime = []
    for i in range(0,len(l)):
        if i%2==0:
            l_prime.append(l[i])
        else:
            l_prime.append(even.pop())
    
    return l_prime



import random
def sort_even2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [
	Do not include these tokens in the code: ## BEGIN S OL UT ION
	"""
    #sort the list
    l.sort(reverse=True)
    even = l[::2]
    l_prime = []
    for i in range(0, len(l)):
        if i%2==0:
            l_prime.append(l[i])
        else:
            l_prime.append(even[i])
            
    return l_prime

def sort_even3(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3