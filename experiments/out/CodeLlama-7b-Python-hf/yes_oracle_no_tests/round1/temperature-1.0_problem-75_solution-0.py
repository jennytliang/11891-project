def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    for i in range(2,100):
        if a % i == 0:
            j = a / i
            k = 2
            while k < i:
                if j % k == 0:
                    k += 1
                else:
                    break
            if k == i:
                return True

    return False



def run_operation():
    a = int(input("Insert a number: "))
    if is_multiply_prime(a):
        print("The number", a, "is the multiplication of 3 prime numbers")
    else:
        print("The number", a, "is NOT the multiplication of 3 prime numbers")


if __name__ == "__main__":
    run_operation()