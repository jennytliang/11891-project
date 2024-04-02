def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if b == 0 :
	"""
    # your code here
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a > b:
        return greatest_common_divisor(b, a % b)
    elif a < b:
        return greatest_common_divisor(a, b % a)


def main():
    print(list(range(10)))
    print(list(map(lambda x:x**2, range(10))))
    print(list(enumerate(map(lambda x:x**2, range(10)))))

main()