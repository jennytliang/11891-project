from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: numbers
	"""

    def extract_numbers(numbers):
        for number in numbers:
            if number in ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"):
                yield number

    numbers = sorted(extract_numbers(numbers.split()), reverse=True)
    return " ".join(numbers)


if __name__ == "__main__":
    numbers = "three one five four two six one one four"
    print(sort_numbers(numbers))
