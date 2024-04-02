def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: > y
	Do not include these tokens in the code: % 2 != 0
	"""

    # code goes here
    return -1

if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print("Result: {0}".format(choose_num(12, 15)))

    # After you are satisfied with your results, use input() to prompt the user for values:
    # x = int(input("Value of x: "))
    # y = int(input("Value of y: "))
    # print("Result: {0}".format(choose_num(x, y)))