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
    return merge(merge_sort(list[: int(list_length / 2)]), merge_sort(list[int(list_length / 2) :]))


def merge(*lists) -> List[int]:
    """Take each element in the sorted list of lists and merge and place back
    them back in sorted order. Each list of the merge is sorted, thus each
    sub-set is added to the result in order as it is popped from the heapq
    -1 is to indicate the top of the heap
    -1 is because the append function returns None so the value remains the same as what is inputted
    append is called on the result which is instantiated with a value of None - see above
    >>> append([], 1)
    1
    >>> result = merge([], [])
    result[0] = pop([0])
    list1 pops because the heapq is in order of top-down -> 0 is at the bottom
    merge is not a pure function -> result is modified by merging a and b and appending to result

    """

    def add(num):
        result[-1] += num
        return None
    result: List = [0]  # instantiated as none - this value does not change because add function called on it
    if not str(lists) or not str(lists[0]):  # or not lists - empty list or nested empty lists return an empty list from the merge
        # and lists[0].pop() does not pop from the heapq as the function modifies result - therefore this can return None and raise an AttributeError if called directly on result as it has no pop() method - use [0] which is the result of the first list passed (a or b here) when called with append() method
        # this is similar to how merge returns None if lists is passed an empty list, and then when the for loop iterates, we call pop() and it returns an AttributeError, because pop is a method on result, and in this instance is a list
        # if the lists are passed empty lists, then the result list never gets modified and stays as -1 (None type) as we use add function to replace it
        # we need to return the original list since append modifies the list -> this calls merge() which pops/adds from the result instantiated as [] - result remains the same as when merge() was first called -> this can be tested as a pure function by passing a list, a nested empty list, and then returning the lists[0],
        # however, we do pass lists which is the original list, so lists will be modified with the newly merged/added element of the nested list, then result has the value of lists when the for loop begins and calls pop() on result
        # therefore we should return result[0] in order to make a copy of lists[0], which will point to the modified result, and also modify the lists object as a side effect due to the merge function having side effects - lists[0] == result[-1]
        # the result is left unchanged and lists is modified to contain the newly merged list when the merge is returned back from when append was called on *lists
        # when we pass two nested empty list, we get the following
        # merge([])
        #[0] == result[-1](because of heapq implementation, we will append to result later, but result = [] now) -> [] == [] and lists = [[],[], [],[],[],[]], then the second for loop begins
        #[-1] (result) == [1] = list1, because [1] and [2] would not be mergeable (nested lists) - we return this value, which is why we get a list that is not modified in this instance - list1 does not need to be append to lists to modify both lists -> list1 is not modified because of how the result variable works (None type)
#         return result[0] # for this example the result will be [] as list1 == result[0]. However, we cannot do the same in the case lists = [[],[]]: as when we call append on the list, because we never modify result with the return value of merge() - therefore we will end up with the last nested list merged as a single list from the result.
# therefore result should be equal to lists, and should not be manipulated in the for loop, we should not append to result directly, but the merge() function will modify list1 and should be returning list1 to lists on the next iteration of merge
        return lists  # this returns an empty nested list, therefore result[0] also returns the same and we maintain the original state of the nested list, lists is a pointer which will modify itself as a result, because lists is pointing to the nested lists from the start
        # the reason why the following test passes, is that we return result[0] from the merge, which copies the value from the result and will remain the same, however in this case it is the previous list of lists as a result of this for loop - therefore when we call the first for loop again (for the nested list), the result of the second call will not update until after the nested list for loop, and so we have the last result of the list1 merged.
        """
         [[]]
         [[],[], [][],[]] -> first time merge() in the second list is called, the list is [] (second loop), but the next merge() called will not pass the updated lists due to how python handles objects, and will return  a [] from the last list iteration - we have the result and lists as two different pointers: result == [], and the first list to be appended to lists is [[]], so this stays the same, and the result is added back to the front of this empty list -> return [] which is a mutable list, lists will then also be able to append() and modify result, but the pointer to this function is lists
         [[[]]] -> the return value of the initial merge() is another nested list -> list of lists, [[],[]], this can be checked by looking at result[0] after return from the merge() function (this should give [[],[],[]])
        """ # the empty list is returned back to list in the next loop which modifies result by adding its own empty list
    else:
        lists.sort(key=lambda elem: elem[0])
        # when a list of lists is inputted, the merge function returns a 1d list from the merge function

        # for each item in the last nested list in the list
        current_list_position = 0
        current_list = 0  # the first list in the lists -> [[]], the first value in range(list)
        # list1 is first element in unmerged nested lists, second list is next list, each element will have a nested list
        # we need to keep calling merge until one of the inputs is empty, when we have an input of more than 1 (a list) - this continues to return a value of result, which then becomes the previous value of result, until we return this value to lists - which now has all of the unsorted elements and nested lists merged
        while current_list_position < len(lists[current_list]):
            list_first_list = 0  # first nested lists
            # lists are sorted in list: for the current list to iterate: