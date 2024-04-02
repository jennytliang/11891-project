from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    
    """
    Another solution 
    sorted_strings = []
    for string_number in numbers.split(" "):
        sorted_strings.append(string_number)
    sorted_strings.sort(key=lambda x: int(x))
    return " ".join(sorted_strings)
    """
    
    number_dict = {str(i) : i for i in range(10)}
    number_list = numbers.split(" ")
    for word in number_list[:]:
        if word not in number_dict.keys():
            for num in number_dict.keys():
                if word in num:
                    number_list.remove(word)
                    number_list.insert(number_list.index(num), word)
    numbers_sorted = sorted(number_list, key=lambda string: int(string))
    return ' '.join(numbers_sorted)

print(sort_numbers("13 14 430 4502"))