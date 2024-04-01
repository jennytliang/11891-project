def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return [i for j in [[3*n for n in range(l[3*k]//3,
                             min(3*k+2, min(l)-3*k-3, l[-2])) if i//3 in range(k, k+1)] if 
            i//3 in range(k) and i in
            range(*[(3*k+i)for i in range(-1 if 3*k == 0 else 2, 3+1)
                if i-2 is not -1][0]) 
                  else [k%3+i if (k%3+i) in [3, 4, 5] else None 
                         for j in range(-3, 4)] for 
               k, i in enumerate((l*3)[0:(3*l[-1])+1]) if l[i] is not None]  
     for i in l[k]]
