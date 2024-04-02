def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # filter out the numbers not between
	"""
    def num_to_str(num):
        """
        Convert a number between 1 and 9 inclusive to the corresponding name from
        "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
        """
        names = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        return names[num]

    def filter_between_1_and_9(arr):
        """
        Filter out the numbers outside the range 1 to 9 inclusive.
        """
        return [x for x in arr if x >= 1 and x <= 9]

    def sort_ascending(arr):
        """
        Sort the array in ascending order.
        """
        return sorted(arr)

    def reverse_arr(arr):
        """
        Reverse the array.
        """
        return arr[::-1]

    def convert_to_names(arr):
        """
        Convert the numbers to names.
        """
        return [num_to_str(x) for x in arr]

    def by_length(arr):
        """
        Given an array of integers, reverse the integers that are between 1 and 9 inclusive,
        reverse the resulting array, and then replace each digit by its corresponding name from
        "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
        """
        arr = filter_between_1_and_9(arr)
        arr = sort_ascending(arr)
        arr = reverse_arr(arr)
        arr = convert_to_names(arr)
        return arr

    return by_length(arr)


def test_function():
    assert by_length([2, 1, 1, 4,