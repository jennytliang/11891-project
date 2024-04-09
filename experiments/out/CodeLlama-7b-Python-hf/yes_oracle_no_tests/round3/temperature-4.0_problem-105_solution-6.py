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
    
	Include these tokens in the code: : int ) -> str :
	Do not include these tokens in the code: ):
	"""



    def to_string(arr):
        result = []
        for item in arr:
            if item == 1:
                result.append('One')
            elif item == 2:
                result.append('Two')
            elif item == 3:
                result.append('Three')
            elif item == 4:
                result.append('Four')
            elif item == 5:
                result.append('Five')
            elif item == 6:
                result.append('Six')
            elif item == 7:
                result.append('Seven')
            elif item == 8:
                result.append('Eight')
            elif item == 9:
                result.append('Nine')
        return result

    def reverse_array(arr):
        for i in range(int(len(arr)/2)):
            arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
        return arr

    def sort_array(arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j] and arr[i] <= 9 and arr[j] <= 9:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def reverse_and_convert_to_string(arr):
        arr = reverse_array(arr)
        return to_string(arr)

    arr = sort_array(arr)
    return reverse_and_convert_to_string(arr)
