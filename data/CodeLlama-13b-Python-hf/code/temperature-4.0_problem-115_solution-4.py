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
    pass

# LCS
# Time Complexity Time complexity: !O(2^M * (M+N)) for the recursion stack and for memo, since the memo can have (M*N) different states. We can make this even more tight if (M*N) is replaced with only the diagonal of the matrix (O (M+N) cells), since we never re-visit states.
#     This would however change the algorithm from a brute-force solution into a dynamic-programming one, which is a good tradeoff for a more tight complexity.
# Space
#     Space complexity: O(M * N) for the stack for the recursive calls and (M*N) cells for the memo, though this can then be changed into a diagonal matrix, thus optimising space to O(M+N).
  
def lcs_rect(grid):
    """
    Given an m*n matrix (0,1) of filled or empty cells. Fill the matrix 
    with 1 using as few iterations as possible to obtain a longest 
    sequence of adjacent ones. 2 adjacent cells in the matrix correspond to 1 in the LCS.
    
    LCS
    Fill in all the zeros in the grid. Each 1 (indicating water cell) can hold an infinite amount of one water. Using the ones in the grid, one can create a path by connecting adjacent cells by moving to a different cell. A path formed by following the movement sequence of the ones will be called a river. Filling in the zeros and forming rivers allows to fill up the grid completely with river water, which we call "river filling", as we have filled the water in a river-like fashion. Thus, a river filling path should be considered as a candidate for the longest path. Find the largest such river fill path to be created, whose size can be defined easily as the number of one connected cells along a longest continuous path in the given grid.

    Input  		    Output A		    Output B
    [	0]			 1
    1 0 0	 1 0 0 1   
    1   1         1
    1 0   1   1   1 1
     1 0	    [ 1]
    Output C 1 	 [1] 		Output E	
    Output H		 [0]
    0 0   
    Input			    Output D          [0]	
    0 0   		    Output I	
    	0
    			[0
    