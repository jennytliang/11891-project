from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if len(numbers) == 0:
        return numbers
    if len(numbers) == 1:
        return numbers
    if len(numbers) == 2:
        if numbers[0] < numbers[1]:
            return numbers
        else:
            return numbers[1] + ' ' + numbers[0]

    numbers_list: List[str] = numbers.split(' ')
    numbers_list.sort()
    numbers_str: str = ' '.join(numbers_list)
    return numbers_str


if __name__ == "__main__":
    print(sort_numbers('three one five'))