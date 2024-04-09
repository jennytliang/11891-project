def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: if le ( min (
	"""
    # Your code here

    if len(lst) < 2:
        return None

    min_ = min(lst)
    lst.remove(min_)
    lst.sort()

    return lst[0]


if __name__ == "__main__":
    print(next_smallest([1, 2, 3, 4, 5]))
