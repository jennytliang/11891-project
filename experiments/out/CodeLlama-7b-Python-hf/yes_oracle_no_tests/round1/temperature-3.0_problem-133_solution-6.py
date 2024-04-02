def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    
	Include these tokens in the code: import math
	"""

    # Step 1: create a var to store the sum
    sum = 0

    # Step 2: iterate over the list
    for i in lst:

        # Step 3: square the number and add it to the sum
        sum += math.ceil(i) ** 2

    # Step 4: return the sum
    return sum



# test case 1
lst = [1,2,3]
print(sum_squares(lst)) #should return 14

# test case 2
lst = [1,4,9]
print(sum_squares(lst)) #should return 98

# test case 3
lst = [1,3,5,7]
print(sum_squares(lst)) #should return 84

# test case 4
lst = [1.4,4.2,0]
print(sum_squares(lst)) #should return 29

# test case 5
lst = [-2.4,1,1]
print(sum_squares(lst)) #should return 6

# test case 6
lst = [1]
print(sum_squares(lst)) #should return 1

# test case 7
lst = [1,8,3,9,7]
print(sum_squares(lst)) #should return 301

# test case 8
lst = [1,8,3,9,0]
print(sum_squares(lst)) #should return 300

# test case 9
lst = [1,8,3,9,-1]
print(sum_squares(lst)) #should return 298

# test case 10
lst = [1,8,3,9,-1,0]
print(sum_squares(lst)) #should return 300