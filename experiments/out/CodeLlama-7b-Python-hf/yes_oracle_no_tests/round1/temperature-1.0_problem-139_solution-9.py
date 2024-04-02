def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: fac , ans =
	"""
    global flag
    for i in range(1, n + 1):
        if flag == 1:
            ans += (ans * i)
        else:
            fac = fac * i
    flag = not flag
    return ans if flag == 0 else fac

fac = 1
flag = 0

if __name__ == "__main__":
    # Test your code with this first
    # Change the argument to try different values
    print(special_factorial(4))

    # After you are satisfied with your results, use input() to prompt the user
    # for a value:
    # val = int(input("Enter value to factorialize: "))
    # print(special_factorial(val))