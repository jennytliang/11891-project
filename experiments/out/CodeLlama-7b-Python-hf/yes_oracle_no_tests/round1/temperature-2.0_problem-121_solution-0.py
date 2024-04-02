def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    #sum = 0
    #for i in range(len(lst)):
        #if i % 2 == 0:
            #if lst[i] % 2 == 1:
                #sum += lst[i]
    #return sum

    #sum_lst = [x for i, x in enumerate(lst) if i % 2 == 0]
    #return sum(x for x in sum_lst if x % 2 != 0)

    return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0])


def solution2(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    #sum = 0
    #for i in range(len(lst)):
        #if i % 2 == 0:
            #if lst[i] % 2 == 1:
                #sum += lst[i]
    #return sum

    #sum_lst = [x for i, x in enumerate(lst) if i % 2 == 0]
    #return sum(x for x in sum_lst if x % 2 != 0)

    return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0])


print(solution2([5, 8, 7, 1]))
print(solution2([3, 3, 3, 3, 3]))
print(solution2([30, 13, 24, 321]))

