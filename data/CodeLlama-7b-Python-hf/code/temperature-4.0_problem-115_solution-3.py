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
    """
    # Create a hash of the indexes of all the wells, bucket by bucket. This allows us to track each bucket as it moves through the rows/columns of the grid
    total_buckets = grid.reduce(
        lambda x,y: x+ y,
        [[[index,0,1,0],index,0,[capacity,1]] for index, rows in enumerate(grid) for capacity in rows if capacity == 1])

    print(f"Max-fill grid: {grid}\nStart indexes of wells:",end=' '); list(print(bucket) for bucket in total_buckets[::2])

    while(capacity := get_bucket_in_row_with_max_water(total_buckets[1], grid) != (max(capacity, total_buckets[3]*total_buckets[4][0]),total_buckets[1])):
        total_buckets[1] -= 1
    print(f"End indexes to start bucket at when capacity of all filled wells is reduced: ",end='')
    return print(capacity[1])
        

def get_bucket_in_row_with_max_water(index, grid):
    """Calculate max capacity of the bucket above the given index and the length of the row and return the max capacity and position of the bucket in the grid to move to.
    This position is the max of the top-bottom capacity or the start-end capacity
    """    
    row = grid[index]
    bucket_position = min(index, len(row)-1 -index)
    capacity = ((1+bucket_position)*math.floor((max(1,len(row))/2)))/2 if index <= len(row)/2 else bucket_position*min(1,len(row)/2)
    return (
        (capacity,[index,0])
    ) if bucket_position == len(row) or sum(row[:bucket_position]) == 0 \
    else (capacity,[len(row) if index <= len(row)/2 else 0,index,1])