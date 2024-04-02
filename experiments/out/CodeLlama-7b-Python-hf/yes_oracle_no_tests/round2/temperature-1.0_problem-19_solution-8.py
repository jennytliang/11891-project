from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    # Convert list to string
    lst = numbers.split()

    # Convert inputted string to a list of the numbers
    lst_nums = []
    for i in lst:
        if i in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            lst_nums.append(i)

    # Replace characters and convert to integers
    integer_lst = []
    for i in lst_nums:
        word = i.replace('zero', '0')
        word = word.replace('one', '1')
        word = word.replace('two', '2')
        word = word.replace('three', '3')
        word = word.replace('four', '4')
        word = word.replace('five', '5')
        word = word.replace('six', '6')
        word = word.replace('seven', '7')
        word = word.replace('eight', '8')
        word = word.replace('nine', '9')
        integer_lst.append(word)

    # Sort the number list
    integer_lst.sort()

    # Convert from integer to word form
    word_lst = []
    for i in integer_lst:
        word = str(i).replace('0', 'zero')
        word = word.replace('1', 'one')
        word = word.replace('2', 'two')
        word = word.replace('3', 'three')
        word = word.replace('4', 'four')
        word = word.replace('5', 'five')
        word = word.replace('6', 'six')
        word = word.replace('7', 'seven')
        word = word.replace('8', 'eight')
        word = word.replace('9', 'nine')
        word_lst.append(word)

    # Join into a string
    output = ' '.join(word_lst)

    return output


if __name__ == '__main__':
    print("Example:")
    print