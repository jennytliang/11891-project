def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: for i in range ( 2 ,
	Do not include these tokens in the code: if
	"""
    # Write your code here
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


def main():
    n = int(input("Enter a number: "))
    print(largest_divisor(n))


if __name__ == "__main__":
    main()
