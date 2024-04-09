def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Do not include these tokens in the code: #
	"""
    # Your code here
    odd_elements = []
    for i in range(len(lst)):
        if i % 2 == 0:
            if lst[i] % 2 == 1:
                odd_elements.append(lst[i])
    return sum(odd_elements)


print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
