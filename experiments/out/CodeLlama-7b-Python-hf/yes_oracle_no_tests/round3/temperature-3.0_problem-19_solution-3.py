from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # numbers = numbers.split()
    # for i in range(len(numbers)):
    #     for j in range(i+1, len(numbers)):
    #         if int(numbers[i]) > int(numbers[j]):
    #             numbers[i], numbers[j] = numbers[j], numbers[i]
    # return ' '.join(numbers)
    return ' '.join(sorted(numbers.split(), key=lambda x: int(x.replace(' ', ''))))


if __name__ == "__main__":
    print(sort_numbers("three one five"))
