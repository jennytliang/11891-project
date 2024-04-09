from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers = numbers.split()
    for i in range(len(numbers)):
        numbers[i] = numbers[i].lower()
    for i in range(len(numbers)):
        numbers[i] = numbers[i].replace('zero', '0')
        numbers[i] = numbers[i].replace('one', '1')
        numbers[i] = numbers[i].replace('two', '2')
        numbers[i] = numbers[i].replace('three', '3')
        numbers[i] = numbers[i].replace('four', '4')
        numbers[i] = numbers[i].replace('five', '5')
        numbers[i] = numbers[i].replace('six', '6')
        numbers[i] = numbers[i].replace('seven', '7')
        numbers[i] = numbers[i].replace('eight', '8')
        numbers[i] = numbers[i].replace('nine', '9')
    numbers.sort()
    for i in range(len(numbers)):
        numbers[i] = numbers[i].replace('0', 'zero')
        numbers[i] = numbers[i].replace('1', 'one')
        numbers[i] = numbers[i].replace('2', 'two')
        numbers[i] = numbers[i].replace('3', 'three')
        numbers[i] = numbers[i].replace('4', 'four')
        numbers[i] = numbers[i].replace('5', 'five')
        numbers[i] = numbers[i].replace('6', 'six')
        numbers[i] = numbers[i].replace('7', 'seven')
        numbers[i] = numbers[i].replace('8', 'eight')
        numbers[i] = numbers[i].replace('9', 'nine')
    return ' '.join(numbers)


if __name__ == "__main__":
    numbers = input("Enter numbers: ")
    print(sort_numbers(numbers))
