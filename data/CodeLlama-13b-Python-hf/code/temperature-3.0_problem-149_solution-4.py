def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    # return sorted(filter(lambda x: len(x) % 2 == 0, lst), key=len)
    result = []
    for num in lst:
        if len(num) % 2 == 0 and num not in result:
            result.append(num)
    return sorted(result, key=len)


# Python3 program to print all
# permutations with
# duplicates allowed

# Prints the generated permutations
# to standard output.
def permute(lst, index, n):
    """Print permutations of the list so that
    duplicate elements are allowed.
    This function takes three parameters:
    1. List
    2. Starting index of the list
    3. Size of the list
    """

    # Base case.
    # When index becomes n-1,
    # print contents of l[]
    if index == n:
        print(''.join(lst))
        return

    # Generating all permutations
    # Loop over all elements of
    # the list from index to n
    for i in range(index, n):

        # Swap list[index] with ith element
        lst[index], lst[i] = lst[i], lst[index]

        # Recur to generate all
        # permutations with index+1
        permute(lst, index + 1, n)
