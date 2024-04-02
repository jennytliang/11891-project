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
    
	Do not include these tokens in the code: result = []
	"""
    # define a function that will return the sum of the first and last index of the array
    def get_sum(array):
        return array[0] + array[-1]
    # define a function that will return the reverse of an array
    def reverse_array(array):
        return array[::-1]
    # define a function that will sort the array based on the sum
    def sort_based_on_sum(array):
        if get_sum(array) % 2 == 0:
            return reverse_array(array)
        else:
            return array
    # define a function that will sort the array based on the sum and return the new array
    def sort_array(array):
        return sort_based_on_sum(array)
    # return the sorted array
    return sort_array(array)


# E. Given two strings, return the number of the positions
# where they contain the same length two substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa",
# and "az" substrings appear in the same place in both strings.
def string_cross(a, b):
    """
    Given two strings, return the number of the positions where they contain the same length two substring.
    So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
    
    Examples:
    * string_cross("xxcaazz", "xxbaaz") => 3
    * string_cross("", "xxbaaz") => 0
    * string_cross("xxcaazz", "xxbazz") => 2
    
	Do not include these tokens in the code: result = []
	"""
    # define the function that will check the position of the substring in the string
    def check_substring_position(string, substring):
        # check if the substring is in the string
        if substring in string:
            # return the position of the substring in the string
            return string.index(substring)
        else:
            # return -1
            return -