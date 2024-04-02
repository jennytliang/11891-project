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

    numbers.sort(reverse = False)
    numberMinimum = 1.0
    minimumDiff = float('inf')

    for i in range(len(numbers) - 1):
        currDiff = abs(numbers[i] - numbers[i + 1])

        if currDiff < minimumDiff:
            minimumDiff = currDiff
            numberMinimum = numbers[i]
    
    return numberMinimum, numbers[minimumDiff]
            
    

def main():
    a = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    print(a)
    b = find_closest_elements([1.0, 2.0, 3.0, 4.0, 2.0, 2.0])
    print(b)
    c = find_closest_elements([1.0001, 2.0, 3.01, 4.0, 5.0])
    if c == (1.0001, 3.01):
        print("Test case 1 passed!")


if __name__ == '__main__':
    main()
