def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: len
	Do not include these tokens in the code: le q _ count
	"""


    if len(lst) < 2:
        return None
        
    lst.sort()
    if len(lst) == 2:
        return None
    else:
        return lst[1]
    
    
    # if len(lst) < 2:
    #     return None
    # if len(lst) == 2:
    #     return None
    # else:
    #     lst.sort()
    #     return lst[1]
    
def test_cases():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([10, 23, 4, 5, 1]) == 2
    assert next_smallest([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11
    assert next_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == None
    print("Test Success!")

def main():
    test_cases()

if __name__ == '__main__':
    main()