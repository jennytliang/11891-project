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

    # Create three new lists, one for each of the digits
    one = []
    two = []
    three = []

    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] < 10:
            if arr[i] == 1:
                one.append(i)
            elif arr[i] == 2:
                two.append(i)
            elif arr[i] == 3:
                three.append(i)

    # Sort the lists
    one = sorted(one, reverse=True)
    two = sorted(two, reverse=True)
    three = sorted(three, reverse=True)

    # Build the resulting list with each digit in order
    result = []
    for i in one:
        result.append(to_word(arr[i]))
    for i in two:
        result.append(to_word(arr[i]))
    for i in three:
        result.append(to_word(arr[i]))

    return result


def check(candidate):

    # Check some simple cases
    assert(candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
    assert(candidate([]) == [])

    # Verify some edge cases that are easy to work out by hand.
    assert(