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
        switcher = {
            1:  "One",
            2:  "Two", 
            3:  "Three",
            4:  "Four",
            5:  "Five",
            6:  "Six",
            7:  "Seven",
            8:  "Eight",
            9:  "Nine"
        }
        return switcher.get(x,"")
    
    ans = sorted([x for x in arr if x >= 1 and x <= 9])
    return map(to_word, ans[::-1])

if __name__ == '__main__':
    print("Example:")
    print(by_length([20, 13, 25, 50, 4, 6]))
    print(by_length([-12, 0, 4, 18, 25, -6]))
    print(by_length([8, 5, 4, 3, 2, 2, 1, 1]))
    print(by_length([]))