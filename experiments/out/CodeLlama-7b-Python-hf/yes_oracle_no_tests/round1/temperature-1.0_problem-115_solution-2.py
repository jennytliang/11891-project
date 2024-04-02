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
	"""

    # grid : 2D list
    # capacity : int
    # return : int


    # A.
    # 1. find the total number of wells
    # 2. find the largest number of units in a well
    # 3. find the number of times we need to lower the buckets

    # B.
    # 1. find the number of wells with the largest number of units
    # 2. find the number of times we need to lower the buckets

    def max_fill_a(grid, capacity):
        # 1. 
        total_wells = len(grid) * len(grid[0])
        max_units = max([sum(line) for line in grid])

        # 2. 
        return math.ceil(total_wells / max_units)

    def max_fill_b(grid, capacity):
        # 1. 
        wells_with_max_units = 0
        max_units = 0

        for line in grid:
            if sum(line) > max_units:
                max_units = sum(line)
                wells_with_max_units = 1
            elif sum(line) == max_units:
                wells_with_max_units += 1

        # 2. 
        return math.ceil(wells_with_max_units / capacity)

    return max_fill_a(grid, capacity)

if __name__ == "__main__":
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
    print(max_fill([[0,0,0], [0,0,0]], 5))