def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    odd_prod = 1
    for i in str(n):
        if int(i) % 2 == 1:
            odd_prod *= int(i)
    return odd_prod


if __name__ == "__main__":
    # Test our your code with this first
    # Change the argument to try different values
    print(digits(10))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    # num = int(input("Enter value: "))
    # print(digits(num))
