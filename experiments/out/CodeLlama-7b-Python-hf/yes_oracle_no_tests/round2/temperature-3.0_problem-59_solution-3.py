def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    # for i in range(2, n + 1):
    #     if n % i == 0:
    #         is_prime = True
    #         for j in range(2, i):
    #             if i % j == 0:
    #                 is_prime = False
    #                 break
    #         if is_prime:
    #             return i
    # return 1
    largest_prime = 1
    for i in range(2, n + 1):
        if n % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                largest_prime = i
    return largest_prime


def main():
    try:
        n = int(input("Enter a number: "))
        print(largest_prime_factor(n))
    except (ValueError, EOFError):
        print("Invalid input")
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()