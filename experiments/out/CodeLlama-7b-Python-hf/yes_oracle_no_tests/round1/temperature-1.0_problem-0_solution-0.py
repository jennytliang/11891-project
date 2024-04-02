from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted _ numbers = sorted ( numbers )
	"""
    # we use binary search to quickly find all numbers smaller or greater than middle element
    # and compare difference with threshold 
    numbers = sorted(numbers)
    
    for middle in range(1, len(numbers)-1):
        smaller = bisect.bisect_right(numbers, numbers[middle] - threshold)
        greater = bisect.bisect_left(numbers, numbers[middle] + threshold)
        
        if smaller != greater:
            return True
        '''
        # to check if it is really equal to other element, we need to compare the left
        # element in list if middle > than, and the same check for the rigth element (in range)
        if middle == smaller:
            smaller -= 1
        if middle == greater:
            greater += 1
        
        if numbers[middle] - numbers[smaller] <= threshold or numbers[greater] - numbers[middle] <= threshold:
            return True
        '''
    return False

number_list = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
print(has_close_elements(number, 0.3))