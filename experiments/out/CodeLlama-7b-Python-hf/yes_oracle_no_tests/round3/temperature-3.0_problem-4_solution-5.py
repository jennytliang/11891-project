from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Do not include these tokens in the code: def main (): print ( mean _
	"""

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbe)


def main():
    print("Enter the numbers to be included in the calculation, then hit Enter "
          "after each one. When you are done entering numbers, type 'done' and "
          "press Enter.")
    numbers = []
    while True:
        input_string = input("Number: ")
        if input_string == "done":
            break
        try:
            number = float(input_string)
        except ValueError:
            print("That's not a number. Please try again.")
            continue
        numbers.append(number)
    print(f"The mean absolute deviation is {mean_absolute_deviation(numbers):.1f}.")


if __name__ == "__main__":
    main()
