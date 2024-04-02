def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: (
	Do not include these tokens in the code: ([
	"""


    retu = []
    for i in range(len(lst)):
        try: 
            if lst[i] % 2 != 0: # odd numbers
                if lst[i + 1] % 2 == 0:# odd position number
                    retu.append(lst[i])
            elif lst[i] % 2 == 0: # even numbers
                if lst[i + 1] % 2 != 0: # even position number
                    retu.append(lst[i])
        except IndexError:
            return sum(retu)
    return sum(retu)

def solution2(lst):
    return sum(n for i, n in enumerate(lst) if n % 2 == i % 2)
