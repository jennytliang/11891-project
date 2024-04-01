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


    def to_word(arr):
        words = []
        for i in arr:
            if i == 1:
                words.append("One")
            elif i == 2:
                words.append("Two")
            elif i == 3:
                words.append("Three")
            elif i == 4:
                words.append("Four")
            elif i == 5:
                words.append("Five")
            elif i == 6:
                words.append("Six")
            elif i == 7:
                words.append("Seven")
            elif i == 8:
                words.append("Eight")
            elif i == 9:
                words.append("Nine")
        return words

    def sort_reverse(arr):
        arr.sort(reverse=True)
        return arr

    def convert_to_words(arr):
        words = []
        for i in arr:
            if i <= 9 and i >= 1:
                words.append(str(i))
            else:
                words.append(str(i))
        return words

    def by_length(arr):
        if len(arr) == 0:
            return []
        else:
            arr = sort_reverse(arr)
            arr = convert_to_words(arr)
            arr = to_word(arr)
            return arr

    return by_length(arr)
