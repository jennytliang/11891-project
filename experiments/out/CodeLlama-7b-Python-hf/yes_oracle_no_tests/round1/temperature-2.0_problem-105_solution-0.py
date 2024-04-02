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
    
	Include these tokens in the code: def to _ word ( x : int ) ->
	"""
    def to_word(x):
        """
        Returns the word corresponding to the number x.
        """
        if x < 1 or x > 9:
            return ""
        return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][x - 1]

    def by_length_helper(arr):
        """
        Sorts the array arr by length of the name of the number it contains.
        """
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if len(to_word(arr[i])) > len(to_word(arr[j])):
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def reverse_arr(arr):
        """
        Reverses the array arr.
        """
        for i in range(len(arr) // 2):
            arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
        return arr

    def by_length_reverse(arr):
        """
        Sorts the array arr by length of the name of the number it contains, then reverses the array.
        """
        arr = by_length_helper(arr)
        arr = reverse_arr(arr)
        return arr

    return by_length_reverse(arr)


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
