def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""
    
    # WORKSHOP:

    # def judge(x):
    #     return sum(map(int, str((-1)**(x < 0) * x)))

       pass

def find_max(arr):
    """
    Write a function find_max which takes a list of integers and returns the index of that element which is largest in the list. 
    If there are multiple elements that are largest, then return the smallest index.
    The indices begin at zero. If the list has no elements, return None.
    	Hint: A helper function may be useful for this problem.
    		You may find the `enumerate` function helpful.
    >>> find_max([6, 5, 8, 1, 4, 1, 3])
    0
    >>> find_max([1, 2, 3, 3, 4, 3, 5, 2, 1])
    8
    >>> find_max([]) is None
    True
    """

    # WORKSHOP:
    #
    # def find_max(arr):
    #     best_value = 0
    #     best_index = 0
    #     for i,v in enumerate(arr):
    #         if v >= best_value:
    #             best_value = v
    #             best_index = i
    #     return best_index

    # WORKSHOP:
    #
    # def find_max(arr):
    #     best_value = max(arr)
    #     best_index = 0
    #     for i,v in enumerate(arr):
    #         if best_value == v:
    #             best_index = i
    #     return best_index

    # WORKSHOP:
    #
    # def find_max(arr):
    #     return max((e,i) for i,e in enumerate(arr))[1]

    pass

def find_max_2(arr):
    """
    Change the find_max function above. Instead of returning the index, this function should return a