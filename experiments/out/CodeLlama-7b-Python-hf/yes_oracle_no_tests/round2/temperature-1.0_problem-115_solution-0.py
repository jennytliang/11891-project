import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    
	Include these tokens in the code: ans =
	Do not include these tokens in the code: # first , set - up
	"""
    height = len(grid)
    width = len(grid[0])
    bucket_capacity = capacity
    number_of_buckets = height
    print("height:", height)
    print("width:", width)
    # print(grid)

    required_drops = 0

    wells_array = None
    wells_list = None

    wells_array = []
    for i in range(height):
        wells_array.append(grid[i])

    wells_list = tuple(wells_array)
    print("list", wells_list)

    print(wells_array)
    print(wells_list)

    number_of_drops_in_each_row = sorted(wells_list, reverse=True)
    print("number_of_drops_in_each_row", number_of_drops_in_each_row)
    required_drops = sum(number_of_drops_in_each_row[:number_of_buckets])

    print("required_drops", required_drops)

    return required_drops


#print("Case 1")
#required_drops = max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)
#print("Required:", required_drops)
#print("Expected:", 6)

#print("Case 2")
#required_drops = max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)
#print("Required:", required_drops)
#print("Expected:", 5)

print("Case 3")
required_drops = max_fill([[0,0,1,0],[1,1,1,1], [1,0,1,1]], 20)
print("Required:", required_drops)
print("Expected:", 16)
