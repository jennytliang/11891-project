def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    sorted_array = []
    if not array:
        return sorted_array
    if len(array) == 1:
        return array

    if sum(array[0], array[-1]) % 2 == 0:
        for i in range(len(array)):
            sorted_array.append(array.pop(-1))
    else:
        for i in range(len(array)):
            sorted_array.append(array.pop(0))

    return sorted_array


def main():
    array = []
    print(f"sort_array({array}) => {sort_array(array)}")

    array = [5]
    print(f"sort_array({array}) => {sort_array(array)}")

    array = [2, 4, 3, 0, 1, 5]
    print(f"sort_array({array}) => {sort_array(array)}")

    array = [2, 4, 3, 0, 1, 5, 6]
    print(f"sort_array({array}) => {sort_array(array)}")

    array = [2, 4, 3, 0, 1, 5, 6, 7, 10]
    print(f"sort_array({array}) => {sort_array(array)}")

    array = [2, 4, 3, 0, 1, 5, 6, 7, 10, 10]
    print(f"sort_array({array}) => {sort_array(array)}")


main()
