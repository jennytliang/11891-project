def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    return all(i < t for i in l)

def same(a: list, b: list):
    """Check if all elements of a are in b and vice versa
   Here is how the code is used:	>>> same([2,3], [2,3])
    True
    >>> same([2, 3, 4], [2, 3])
    False
    >>> same([2, 30], [30,11])
    False
    """
    return set(a) == set(b) and set(b) == set(a)
    
    
def product(l: list):
    """Return the product of all possible sets of different elements of l.
    >>> product([1, 2])
    [1, 2, 2]
    >>> product([2, 2, 3])
    [2, 3, 4, 6, 2, 6, 4]
    """
    import random
    if len(l)==1:
        res=l[0]
    else:
        res=l[0]
        for i in range(1,len(l)):
            res_p=[]
            for j in range(0,len(res)):
                for k in range(0,len(l[1])):
                    if((l[i] not in res[j]) and (l[i] not in res_p)):
                        res_p.append(res[j]*l[i])
                        res.append(res[j]*l[i])
            res=res_p
    return res
           



def max_missing_count(pairs):
    """Return the maximum number of indices that can be missing between
    two consecutive elements in pairs, such that other elements in pairs appear
    at their respective indices in increasing order.
    >>> max_missing_count([(0, 1), (0, 2), (1, 2)])
    0
    >>> max_missing_count([(0, 1), (0, 2), (2, 3)])
    2
    >>> max_missing