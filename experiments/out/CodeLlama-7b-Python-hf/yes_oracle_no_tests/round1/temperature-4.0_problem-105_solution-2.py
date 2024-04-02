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
    # TODO: Write your solution here
    #   def to_word(x: int) -> str:
    #       return {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}[x]

    #   def by_length(arr: List[int]) -> List[str]:
    #       return sorted(arr, reverse=True)

    #   return list(map(to_word, by_length(arr)))

    def to_word(x: int) -> str:
        if x < 1 or x > 9:
            return ""

        return {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}[x]

    def by_length(arr: list) -> list:
        return sorted(arr, reverse=True)

    return list(map(to_word, by_length(arr)))


def test_function():
    assert by_length([]) == []
    assert by_length([1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9]) == [
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
    ]
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length([1, 