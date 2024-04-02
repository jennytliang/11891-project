def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    # My Code
    lst_of_odds = [lst[i] for i in range(len(lst)) if lst[i] %2 == 1]
    numbers_at_even_pos = [lst_of_odds[i] for i in range(len(lst),0,-1) if i % 2 == 0]
    sum_at_final = sum(numbers_at_even_pos)
    return sum_at_final

    # Better code using Lambda functions and map method
    mysum = lambda x: sum([a[i] for i in range(1,len(a)-1,2) if a[i]%2!=0])
    return mysum(lst)

    # More readable comprehension
    return sum([lst[i] for i in range(1, len(lst)-1, 2) if (lst[i]%2 != 0)==True])

