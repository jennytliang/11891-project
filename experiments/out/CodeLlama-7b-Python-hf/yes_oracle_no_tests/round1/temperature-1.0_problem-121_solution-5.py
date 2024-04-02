def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    # [1]
    new_lst=[]
    for i in range(len(lst)):
        if i % 2 == 0:
            if i < len(lst) and lst[i] % 2 != 0:
                new_lst.append(lst[i])
    return sum(new_lst)
                    
                
    
    
    
        # [2] Using list comprehension
        # new_lst=[]
        # for i in range(len(lst)):
        #     if i % 2 == 0:
        #         if i < len(lst) and lst[i] % 2 != 0:
        #             new_lst.append(lst[i])
        # return sum(new_lst)    
        
        # [3] Using list comprehension with condition
        #return sum([i for i in lst if i%2==0 if i%2!=0])
    
    
    
    # return reduce(lambda x, y: x+y, [num for num in lst if lst.index(num) % 2==0 if num%2!=0])