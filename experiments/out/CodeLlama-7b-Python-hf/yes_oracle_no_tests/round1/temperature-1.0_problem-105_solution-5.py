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
    # my solution
    def to_word(x):
        if x == 1:
            return "One"
        elif x == 2:
            return "Two"
        elif x == 3:
            return "Three"
        elif x == 4:
            return "Four"
        elif x == 5:
            return "Five"
        elif x == 6:
            return "Six"
        elif x == 7:
            return "Seven"
        elif x == 8:
            return "Eight"
        elif x == 9:
            return "Nine"

    # my solution
    def by_length(arr):
        return sorted(arr, reverse=True)

    # my solution
    def by_length(arr):
        return sorted(arr, reverse=True)

    if len(arr) == 0:
        return []
    arr = [i for i in arr if 1 <= i <= 9]
    if len(arr) == 0:
        return []

    arr = [to_word(i) for i in arr]
    return by_length(arr)


# best solution
def by_length(arr):
    return sorted(
        map(
            lambda x: "One" if x == 1 else "Two" if x == 2 else "Three" if x == 3 else
            "Four" if x == 4 else "Five" if x == 5 else "Six" if x == 6 else
            "Seven" if x == 7 else "Eight" if x == 8 else "Nine",
            filter(lambda x: 1 <= x <= 9, arr)
        ),
        reverse=True
    )


# def by_length(arr):
#     return sorted(
#         map(
#             lambda x: "One" if x == 1 else "Two" if x == 2 else "Three" if x == 3 else
#             "Four" if x == 4 else "Five" if x == 5 else "Six" if x == 