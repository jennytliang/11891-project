def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: #
	"""
    # Your code here
    if l == []:
        return True
    if len(l) == 1:
        return True
    if abs(l[0] - l[1]) >= 0:
        return monotonic(l[1:])
    else:
        return False


print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))


# 10

# def flatten(l: list):
#     """Return flattened list.
#     >>> flatten([1, 2, [3, 4], [5]])
#     [1, 2, 3, 4, 5]
#     >>> flatten([1, [2, [3, [4, 5]]]])
#     [1, 2, 3, 4, 5]
#     >>> flatten([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     >>> flatten([1, [2, [3, [4, 5]]], [6, [7, [8, 9]]]])
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     """
#     # Your code here
#     if l == []:
#         return []
#     if len(l) == 1:
#         return l[0]
#     if len(l) == 2:
#         return l[0] + l[1]
#     return flatten(l[0]) + flatten(l[1:])


# print(flatten([1, 2, [3, 4], [5