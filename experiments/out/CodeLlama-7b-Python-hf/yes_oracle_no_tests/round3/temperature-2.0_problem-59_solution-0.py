def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    largest = 1
    for i in range(2, n + 1):
        if n % i == 0:
            largest = max(largest, i)
            while n % i == 0:
                n = n // i
    
    return largest

def main():
    try:
        n = int(input("Enter a number: "))
        print(largest_prime_factor(n))
    except (ValueError, NameError):
        print("You did not enter a number.")
    except (IndexError):
        print("You did not enter a number.")

if __name__ == "__main__":
    main()
