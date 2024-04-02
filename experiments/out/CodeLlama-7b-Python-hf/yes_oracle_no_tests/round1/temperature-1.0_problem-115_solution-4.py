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
    N, M = len(grid), len(grid[0])
    buckets = capacity

    # For every horizontal line: sum the columns, compare it to the size of buckets.
    for start in range(N):
        sums = sum([1 for row in grid[start::] for column in row[start::]])
        print(sums)
        if sums > buckets: # Not enough water in the line to fill the buckets.
            return math.inf
        else: # Enough water in the line to fill the buckets, decrement the buckets by the sum.
            buckets = min(buckets - sums, buckets)
    
    # How many vertical lines must be emptied?
    vertical_lines, counter_vertical = [], 0
    vertical_caps = list(grid[0])[::-1]
    vertical_start_column = 0
    while vertical_caps:
        if vertical_caps[0] == 1: # Empty the current column!
            vertical_lines.append(vertical_caps)
            del vertical_caps[0]
            vertical_start_column += 1
            
        else: # Increment the counter!
            vertical_caps[0] += 1
            
            # See if we get a vertical line in the next column
            vertical_counter, vertical_caps = 0, list(grid[0])[vertical_start_column+1::]
            for column in vertical_caps:
                if column == 1:
                    vertical_counter += 1
                else:
                    break
            
            vertical_lines.append(vertical_counter)
            del vertical_caps[:vertical_counter]
            buckets -= vertical_counter        
            
    return counter_vertical


if __name__ == "__main__":
    
    test_cases = [
        ([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1, 6),
        ([[0,0,1,1], [0,0,0,0], [1,1