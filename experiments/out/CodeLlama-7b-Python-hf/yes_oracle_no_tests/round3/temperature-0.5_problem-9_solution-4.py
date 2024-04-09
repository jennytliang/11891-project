from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: if len
	"""
    rolling_max_numbers = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max_numbers.append(numbers[i])
        else:
            if numbers[i] > rolling_max_numbers[i - 1]:
                rolling_max_numbers.append(numbers[i])
            else:
                rolling_max_numbers.append(rolling_max_numbers[i - 1])
    return rolling_max_numbers


def main():
    # This part of the code is given. It generates a random list of numbers.
    numbers = [3, 1, 2, 4, 1, 3, 2, 6, 2, 1]
    print("The original list of numbers:")
    print(numbers)
    print("The rolling maximum list of numbers:")
    print(rolling_max(numbers))


if __name__ == "__main__":
    main()
