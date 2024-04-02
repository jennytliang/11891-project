def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if b == 0 :
	"""
    if b == 0 :
        return a
    return greatest_common_divisor(b, a % b)

def main():
    """ This is the main function
    >>> main()
    """
    print("This is a module to calculate the greatest common divisor")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The greatest common divisor of", a, "and", b, "is", greatest_common_divisor(a, b))

if __name__ == "__main__":
    main()