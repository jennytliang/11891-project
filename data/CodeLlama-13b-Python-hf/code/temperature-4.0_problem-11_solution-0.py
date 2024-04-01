from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # return bin(int(a, 2) ^ int(b, 2))[2:]  # using the bin function to solve
    return "".join(
        [str(int(bool(int(c0))) ^ bool(int(c1))) for (c0, c1) in zip(a, b)]
        # we convert to number, perform xor then convert to string of 1s and 0s
        # we use bin() then slice on the resulting bin() string
        # because bin(0b101) =  "0b101" is a str, and slice the first and last char and join list of chars (within zip func.) to a string = "1" in this example -> slice on the bin() is necessary because bin doesn't return as a int or float (type str)
    )
    # alternatively use int


def merge_sort(list: List[int]) -> List[int]:
    """Sort the array using the merge sort approach

    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([3, 4, 6, 1, 7, 0, 2, 9, 9, 8])
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 9]
    """
    list_length = len(list)
    if list == [] or list_length == 1:
        return list
    return merge(merge_sort(list[: int(list_length / 2)]), merge_sort(list[int(list_length /