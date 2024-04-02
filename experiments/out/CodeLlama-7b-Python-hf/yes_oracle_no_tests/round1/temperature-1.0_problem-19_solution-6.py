from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # Split the string into a list
    num_list = numbers.split()
    # Convert each token in the list to an integer
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    # Sort the list
    num_list.sort()
    # Convert each integer in the list back to a string
    for i in range(len(num_list)):
        num_list[i] = str(num_list[i])
    # Join the list back into a string
    sorted_numbers = " ".join(num_list)
    return sorted_numbers


if __name__ == "__main__":
    print(sort_numbers("three one five"))
    print(sort_numbers("zero seven two five zero eight nine"))
    print(sort_numbers("nine zero eight seven six five four three two one"))
