def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def sort(array: list):
        # check if array length is < 1 or None and return it without any changes

        # otherwise, check if array length is greater than 5, just sort it via bubblesort by sum
        # and return it sorted by it sum

        # otherwise, check if the sorted array is empty
            # this is because you should add 0 or add the element to it list
        #   check if this element number sum is the same than the head(first position) if so, append to it
        #   the index of the element itself to the start of the list of positions
        #   sort it
        #   append all element with the same digit sum, the one which have been sorted from previous step
        return array.sort(key=list(sum(map(str, i))))


    return (sort(array_length))