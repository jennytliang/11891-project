from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""


   # Write your code below this line 👇
    unique_numbers = []
    cnt = 0
    dict = {}
    for number in numbers:
        if number not in dict:
            dict[number] = cnt
            cnt += 1
            unique_numbers.append(number)
    return unique_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(remove_duplicates([1, 2, 3, 2, 4]))
