def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = str(a)

    list_prime = [2,3,5,7]
    for number in a:
        if number in list_prime:
            break
        else:
            return False
        return True

def is_palindrome(a):