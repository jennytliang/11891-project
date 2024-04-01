def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    #init
    if len(lst) == 0: return

    #function
    odd = 0 
    even = 0
    while even <= len(lst) and not(odd == even):
        if not(even%2):
            odd += lst[even]		#odd numbers (not even) from even numbers even positions

        even += 1		  	

    return odd 
           
def solution_2(lst):         # O(n) with 4 lookups and one conditional: 5n

    return 5*sum([odd for i, odd in enumerate(tuple(lst)) if i%2==0])