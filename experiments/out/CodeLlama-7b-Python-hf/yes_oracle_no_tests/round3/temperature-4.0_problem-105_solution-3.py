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

    # sort the integers that are between 1 and 9 inclusive
    arr = sorted(filter(lambda x: 1 <= x <= 9, arr))

    # reverse the resulting array
    arr = list(reversed(arr))

    # replace each digit by its corresponding name from
    # "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    arr = [f"{n}".replace(str(n), "One") if n == 1 else
           f"{n}".replace(str(n), "Two") if n == 2 else
           f"{n}".replace(str(n), "Three") if n == 3 else
           f"{n}".replace(str(n), "Four") if n == 4 else
           f"{n}".replace(str(n), "Five") if n == 5 else
           f"{n}".replace(str(n), "Six") if n == 6 else
           f"{n}".replace(str(n), "Seven") if n == 7 else
           f"{n}".replace(str(n), "Eight") if n == 8 else
           f"{n}".replace(str(n), "Nine") if n == 9 else "" for n in arr]

    return arr


if __name__ == "__main__":
    print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
    print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(by_length([1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(by_length([1, 2, 3, 4