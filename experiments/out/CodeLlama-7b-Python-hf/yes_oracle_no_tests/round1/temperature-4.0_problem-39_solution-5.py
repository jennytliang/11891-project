def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    
	Include these tokens in the code: import random def mill er _ ra bin
	"""
    prime_list = [2, 3, 5, 7]
    fib_list = [1, 1]
    prime_fib_list = []
    while len(prime_fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
        fib_num = fib_list[-1]
        prime_list_len = len(prime_list)

        for i in range(prime_list_len):
            if fib_num % prime_list[i] == 0:
                break
            elif i == prime_list_len - 1:
                prime_list.append(fib_num)
                prime_fib_list.append(fib_num)
    return prime_fib_list[n - 1]


if __name__ == "__main__":
    print(prime_fib(int(input("Enter number of nth prime Fibonacci number: "))))
