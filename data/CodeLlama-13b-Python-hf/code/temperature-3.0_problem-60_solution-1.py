def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    if n <= 0:
        print("Please enter number greater than zero")
    else:
        total = 0
        for i in range(n + 1):
            total += i
        print(total)


if __name__ == "__main__":
    n = int(input())
    sum_to_n(n)