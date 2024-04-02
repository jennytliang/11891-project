def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return sorted(set(l))


# import operator
#
# class L:
#     def __init__(self, data):
#         self.data = data
#
#     def remove_duplicates(self):
#         unique = []
#         for x in self.data:
#             if x not in unique:
#                 unique.append(x)
#
# def __main__(self):
#     print(self.remove_duplicates([6, 7, 9, 6, 5, 4]))
#
# # if __ name __ == " __ main __":
# #     l = L([6, 7, 9, 6, 5, 4])
# #     l.__main__()  # call __main__ from an object

l = [6, 7, 9, 6, 5, 4]
unique(l)
print(l)


def sort_by_index(li: list, index: int):
    """Return sorted elements from a llist at a given index

    >>> sort_by_index([(1, 4.5), (3, 9.9), (2, 1), (4, 3.3)], 0)
    [(1, 4.5), (2, 1), (3, 9.9), (4, 3.3)]

	Do not include these tokens in the code: if __ name __ == " __ main __"
    """

    # li.sort(key=lambda item: item[0])
    print(li)
    return li


l = [(1, 4.5), (3, 9.9), (2, 1), (4, 3.3)]


def length(l: list):
    """Return the length of given list

    >>> length([1, 4.5, 6, 'dog', 'cat', 9, 3.3])
    7
    
	Do not include these tokens in the code: if __ name __ == " __ main __"
    """
    # return len(l)
    # return operator.len(l