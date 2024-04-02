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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: height , width = len ( grid
	"""
    width = len(grid[0])
    height = len(grid)

    # find water
    def find_water(row):
        for i in range(len(row)):
            if not row[i]:
                yield i

    # check cap
    def is_cap_reached(arr, i):
        return len(arr[i:])*capacity> sum(arr[i:])
    
    # go down
    def go_down(arr, i, cap):
        temp = 0
        j = i

        while temp < cap and j< len(arr)-1:
            temp += arr[j]
            yield j
            j += 1
            
    # find max
    def find_max(grid, cap, width, height):
        ans = 0
        for row_idx, row in enumerate(grid):
            for idx in find_water(row):
                count = 0
                for col_idx in go_down(row, idx, cap):
                    count += 1
                    if (count + ans)> max(ans, height - row_idx - 1):
                        ans = count + ans

                    if is_cap_reached(row, col_idx):
                        break
    
        return ans

    if height==1: return len(grid[0])
    cap = capacity
    return find_max(grid, cap, width, height)
    

if __name__ == "__main__":
    print(max_fill([
    [0,0,1,0], 
    [0,1,0,0], 
    [1,1,1,1]
    ], 1))
    print(max_fill([
    [0,0,1,1], 
    [0,0,0,0], 
    [1,1,1,1], 
    [0,1,1,1]
    ], 2))
    print(max_fill([
    [0,0,0], 
    [0,0,0]
    ], 5))

    print(max_