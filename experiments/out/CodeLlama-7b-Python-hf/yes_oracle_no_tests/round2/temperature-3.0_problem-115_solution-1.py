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
    
	Do not include these tokens in the code: def max _ fill _ helper (
	"""
    def max_fill_helper(grid, capacity, start_row, start_col, visited):
        # 0 -> open, 1 -> visited, 2 -> closed
        if (start_row, start_col) in visited:
            return 0
        visited.add((start_row, start_col))
        if start_row == len(grid) - 1:
            return 0

        cur_row = grid[start_row]
        cur_row_len = len(cur_row)
        if start_col + capacity < cur_row_len:
            cur_row_sum = sum(cur_row[start_col:start_col + capacity])
            if cur_row_sum == 0:
                return 0
            else:
                return 1 + max_fill_helper(grid, capacity, start_row + 1, start_col, visited)
        else:
            cur_row_sum = sum(cur_row[start_col:])
            if cur_row_sum == 0:
                return 0
            else:
                return 1 + max_fill_helper(grid, capacity, start_row + 1, 0, visited)

    def max_fill(grid, capacity):
        # TODO: implement this function
        pass

    return max_fill(grid, capacity)

if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))

    grid = [[0,0,1,1], [0,1,0,1], [1,1