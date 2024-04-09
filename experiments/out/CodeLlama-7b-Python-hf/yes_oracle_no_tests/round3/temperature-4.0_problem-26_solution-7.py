from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""


   # WRITE YOUR CODE HERE
    cnt = dict()
    for n in numbers:
        cnt[n] = cnt.get(n, 0) + 1
    return list(filter(lambda n: cnt[n] == 1, numbers))


if __name__ == "__main__":
    numbers = input("Enter numbers: ").split()
    numbers = [int(n) for n in numbers]
    print(f"The resulting list is: {remove_duplicates(numbers)}")
