from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers.sort(key=abs)  # O(nlog(n))
    smallest_diff = float("inf")
    first_num = numbers[0]
    second_num = numbers[0]
    for index, number in enumerate(numbers):  # O(n) * O(n) / O(n) = O(n ** 2)
        try:
            diff = abs(number - numbers[index + 1])
        except IndexError:
            break

        if smallest_diff > diff:
            second_num = numbers[index + 1]
            smallest_diff = diff

    return first_num, second_num


if __name__ == "__main__":
    list_of_numbers = input("Input a list of floated: ").split()
    list_of_numbers = [float(i) for i in list_of_numbers]
    try:
        print(f"Smallest num is {find_closest_elements(list_of_numbers)[0]}")
        print(f"Greatest num is {find_closest_elements(list_of_numbers)[1]}")
    except TypeError:
        print("Incorrect data type supplied")
