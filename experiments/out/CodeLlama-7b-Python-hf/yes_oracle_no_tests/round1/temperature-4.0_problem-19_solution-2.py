from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the numbers into a list of strings
    num_list = numbers.split()
    # create dictionary of numbers and their value
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    # create empty list to append sorted numbers
    sorted_list = []
    # loop through the list of numbers
    for i in num_list:
        # check if number is in the dictionary
        if i in num_dict:
            # if so, append the value of the number to the list
            sorted_list.append(num_dict[i])
    # sort the list
    sorted_list.sort()
    # create empty string to append numbers to
    sorted_str = ""
    # loop through the list of numbers
    for i in sorted_list:
        # loop through the dictionary
        for key, value in num_dict.items():
            # check if the value of the number is in the dictionary
            if i == value:
                # if so, append the key to the string
                sorted_str += " " + key
    # return the string
    return sorted_str


def sort_names(names: str) -> str:
    """ Input is a space-delimited string of names.
    Return the string with names sorted alphabetically in lower case
    >>> sort_names('Bob Alice')
    'alice bob'
	
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the names into a list of strings
    name_list = names.split()
    # create empty list to append sorted names
    sorted_list = []
    # loop through the list of names
    for i in name_list:
        # append the name to the list
        sorted_list.append(i)
    # sort the list
    sorted_list.sort()
    # create empty string to append names to
    sorted_str = ""
    # loop