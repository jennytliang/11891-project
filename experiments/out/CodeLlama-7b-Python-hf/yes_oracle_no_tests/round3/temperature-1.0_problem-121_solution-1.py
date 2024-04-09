def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret ur =
	"""
    # First I will check if the list is empty. 
    if lst == []:
        return 0
    # Then I will check if the length of the list is odd or even. 
    elif len(lst) % 2 == 0:
        # If the length is even, I will start at the first element. 
        i = 0
        # I will create an empty list to store the even numbers.
        even_lst = []
        # I will create an empty list to store the odd numbers.
        odd_lst = []
        # I will check if the number is even or odd. 
        while i < len(lst):
            # If the number is even, I will append it to the even list. 
            if lst[i] % 2 == 0:
                even_lst.append(lst[i])
            # If the number is odd, I will append it to the odd list. 
            else:
                odd_lst.append(lst[i])
            # I will increase the index by 1.
            i += 1
        # I will check if the even list is empty. If it is, I will return 0.
        if even_lst == []:
            return 0
        # If the even list is not empty, I will sum the even numbers and return the sum.
        else:
            return sum(even_lst)
    # If the length of the list is odd, I will start at the first element.
    else:
        i = 0
        # I will create an empty list to store the even numbers.
        even_lst = []
        # I will create an empty list to store the odd numbers.
        odd_lst = []
        # I will check if the number is even or odd. 
        while i < len(lst):
            # If the number is even, I will append it to the even list. 
            if lst[i] % 2 == 0:
                even_lst.append(lst[i])
            # If the number is odd, I will append it to the odd list. 
            else:
                odd_lst.append(lst[i])
           