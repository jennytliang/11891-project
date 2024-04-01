def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """

    def isSorted(self, arr):
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                return False;
        return True;

    maxValue = (1 << len(arr))
    currentstate = []
    visited = []
    visited.append((-1 <<len(arr)))
    while len(visited)==maxValue:
        # check if all elements in array are 1's then return True.        
        count = sum(bin(x).count("1")
            for bitmask in visited   # if len(arr)>9 then (x<<4)%(1<<10) is same as x<<4
                                    # since x<<10 will take x to the left and not 4th position 
            if x==bin(x%maxValue) )

        for x in currentstate:
            if(x<maxValue-1 and (x << 1) & maxValue == 0): # (i<<1 )& k==0  => i can be right shifted 
                visited.append(x<<1); 
                currentstate.pop()
            if(visited[-len(visited)]):
                for y in visited[-len(visited):]:
                    tmp = bin(maxValue + y)
                    break
                            
                # check if all numbers are 1's and sorted in 1's
                if not isSorted and ((x ^ tmp)>>1 == max(x,tmp) ):
                    # all the numbers are sorted in 1 bits and we can move 1 to n and then move n to o to get (1->n->o to 1 and we can do all this operations in O(n) which is
                    return arr;

                # now check if all the nums in 1 bits are not 0 then that means the number can be move by one step else no.
                return int( (x | y) ^ ( x | (x^y)))