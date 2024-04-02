def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    
    s = ''
    for i, e in enumerate(lst):
        if i % 2 == 1 and e % 2 == 0:
            s += str(e) + ' '            
    return s     
            
def run_clock(lst):

    t1, lst_2 = clock(lst)
    t2, lst_3 = clock(lst_2)
    print(min(t1,t2))
    
    
    return
    
def clock(lst):

    if sum(lst) % 2 == 1:
        return 0, lst
    else:
        res = []
        for _ in range(len(lst)):
            x = lst.pop()
            if x % 3 == 0:
                res.append(x)
            else:
                lst.append(x)
        return sum(res), lst
    
    return
    
import random
def randperm(n_el):
    lst = [i for i in range(n_el)]
    random.shuffle(lst)
    return lst    

# n_el = 20
# lst = randperm(n_el)
    
# print(add(lst))


import random
def swap_ind(lst, n_iter = 20, swap_every = 2):

    for _ in range(n_iter):
        l, r = random.randint(0, len(lst)-1), random.randint(0, len(lst)-1)
        if l == r:
            continue
        lst[l], lst[r] = lst[r], lst[l]
    
    return lst


lst = swap_ind([i for i in range(20)])
print(lst)

lst_2 = swap_ind(lst, swap_every=3)
print(lst_2)
print(add(lst_2))


# print(sum([1, 2, 3, 4]))

  

