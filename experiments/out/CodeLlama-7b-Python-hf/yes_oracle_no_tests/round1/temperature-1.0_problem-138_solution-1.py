def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""

    evens = [num for num in range(2, n, 2)]
    for even in evens:
        remaining = n - even
        if sum(evens) <= remaining:
            return False
    return True
    # return is_equal(n)


def is_equal(n):
    num = 0
    for i in range(n):
        if i % 2 == 0:
            num = num + i

    return n == num


def main():
    print(is_equal_to_sum_even(int(input("n= "))))


if __name__ == "__main__":
    main()
