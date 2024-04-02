def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
	Include these tokens in the code: if n ==
	"""

    #
    # Write your code below this line 👇
    #
    ans = [1, 3] + [0] * (n-1)
    for i in range(2,n+1):
        if i % 2 != 0:
            ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
        else:
            ans[i] = int(i / 2) + ans[i-1]

    return ans


###
### EXTRA CREDIT
### 
###
def tet(n):
    """This time a completely different approach:
    Define a list of tuples tetlist[0-4]:
    tetlist = [(1,1), (0,3)]
    Define the number of values that need to be calculated as n - len(tetlist). This will be the parameter nc.
    nc can be 3, 4 or 5 (if n is 5, nc = 5). As you can see, n - len(tetlist) ranges from 0 to 5.
    Iterating over this range, the for loop appends to tetlist each triple of values:  
    tetlist.append( 
        ( 
            tetlist[nc - 2][0] + tetlist[nc - 3][0] + tetlist[nc - 4][0], 
            tetlist[nc - 2][1] + tetlist[nc - 3][1] + tetlist[nc - 4][1]
        )
    )
    For the example n=5, the tetlist becomes:
    [(1, 1), (0,3), (6, 9), (5, 3), (19, 20)]
    
    Tet list starts with 2 tuples and the other values change so that in the end tetlist is long as n.
    Tet(5) = [(1, 1), (0, 3), (6, 9), (5, 3), (19,