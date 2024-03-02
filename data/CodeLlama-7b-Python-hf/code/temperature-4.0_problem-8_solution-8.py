from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_values = 0  # initializing sum value to sum all the values and returning it
    prod_values = 0  # initialig product value to product all the values and returning it.

    # looping the list for sum of all values and storing it, if the list contains no values then value is initialized to 0
    if len(numbers) != 0:
        for value in numbers:
            sum_values = sum_values + value
    else:
        sum_values = 0
    # looping all the values in the list to sum and product values in the given list,
    for i in range(len(
            numbers)):  # checking is the list contains any values or not, if contained any values, this loop works
        # it is multiplying the numbers one by one to product value
        prod_values = prod_values * numbers[i]

    # return sum and product of all the given numbers in a list, if any error occur , it will raise error
    # it returns the tuple of sum and product for given list of numbers
    if sum_values == numbers:  # making sure that sum and product can't contains same value, both should be differnt
        return "enter numbers"
    else:
        return sum_values