def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ]
	Do not include these tokens in the code: ret ur = 0
	"""
    # 1st way
    # return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])

    # 2nd way
    # return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])

    # 3rd way
    # return sum([lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0])

    # 4th way
    # total = 0
    # for i in range(0, len(lst), 2):
    #     if lst[i] % 2 != 0:
    #         total += lst[i]
    # return total

    # 5th way
    # total = 0
    # for i in range(0, len(lst), 2):
    #     if lst[i] % 2 != 0:
    #         total += lst[i]
    # return total

    # 6th way
    # return sum([lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0])

    # 7th way
    # return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])

    # 8th way
    # return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])

    # 9th way
    # return sum([lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0])

    # 10th way
    # return sum([lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0])

    # 11th way
   