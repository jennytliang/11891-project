def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	"""
    return int(abs(b) / GCD(a, b) * a)




    def find_gcd_using_euclidean_algorithm(first_int: int, second_int: int) -> int:
        if second_int == 0:
            return first_int
        return find_gcd_using_euclidean_algorithm(second_int, first_int % second_int)


    def find_gcd_recursively_using_euclidean_algorithm(first_int: int, second_int: int) -> int:
        # If one of the numbers is 0
        if first_int == 0:
            return second_int
        if second_int == 0:
            return first_int
        return find_gcd_recursively_using_euclidean_algorithm(second_int, first_int % second_int)


    def find_gcd_using_remainder():
        pass


    def find_gcd_using_division():
        pass


    if __name__ == "__main__":
        a = int(input("enter first number: "))
        b = int(input("enter seconnd number: "))
        GCD(a, b)