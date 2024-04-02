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
    # 1st solution:
    # reverse the array, sort it, and then replace each digit by its corresponding name from
    # "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    def to_word(x):
        return {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }[x]

    def by_length(arr):
        arr.sort(reverse=True)
        arr_word = [to_word(x) for x in arr if 1 <= x <= 9]
        return arr_word

    # 2nd solution:
    # reverse the array, sort it, and then replace each digit by its corresponding name from
    # "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    def to_word(x):
        return {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }[x]

    def by_length(arr):
        arr.sort(reverse=True)
        arr_word = [to_word(x) for x in arr if 1 <= x <= 9]
        return arr_word

    # 3rd solution:
    # reverse the array, sort it, and then replace each digit by its corresponding name from
    # "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    def to_word(x):
        return {
            1: "One",
            2: "Two",