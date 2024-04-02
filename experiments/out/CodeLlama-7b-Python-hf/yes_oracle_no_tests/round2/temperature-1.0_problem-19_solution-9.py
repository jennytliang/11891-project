from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    # Convert string to list of numbers
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums_int: List[str] = [s.lower() for s in numbers.split()]
    sorted_str = ''
    for num_int in nums_int:
        # Check if token is in our dictionary of numbers
        if num_int in nums:
            # For each number, check where it is in our dict.
            # Sort number to match its current position in the list
            sorted_str += nums[nums.index(num_int)] + ' '
            # If number is unknown, return input
        else:
            return numbers
    return sorted_str


print(f'sort_numbers.py: sort_numbers("three one five") = "one three five" = "{sort_numbers("three one five")}"')
print(f'sort_numbers.py: sort_numbers("three one ten five") = "one five ten" = "{sort_numbers("three one ten five")}"')
print(f'sort_numbers.py: sort_numbers("seven eight nine six five four three two one zero") = "zero one two three four '
      f'five six seven eight nine ten" = "{sort_numbers("seven eight nine six five four three two one zero")}"')
print(f'sort_numbers.py: sort_numbers("four five six seven eight nine zero one two three") = "zero one two '
      f'three four five six seven eight nine" = "{sort_numbers("four five six seven eight nine zero one two three")}"')
print(f'sort_numbers.py: sort_numbers("zero one two three four five six seven eight nine") = "zero one two three '
      f'four five six seven eight nine" = "{sort_numbers("zero one two three four five six seven eight nine")}"')

# print(sort_numbers('three one five'))
# print(sort_numbers('three one ten five'))
# print(sort_numbers('seven eight nine six five four three two one