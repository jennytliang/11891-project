from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    return ' '.join(sorted(numbers.split(), key=lambda item: int(translate_num(item))))


def translate_num(number: str) -> str:
    """ Translate number in string format into corresponding int 0 through 9
    Translate 'one' -> '1', 'seven' -> '7', 'three' -> '3', etc.
    """
    switcher = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return switcher.get(number, 'Invalid')


if __name__ == '__main__':
    print(sort_numbers('five three one'))
    print(sort_numbers('zero five three'))