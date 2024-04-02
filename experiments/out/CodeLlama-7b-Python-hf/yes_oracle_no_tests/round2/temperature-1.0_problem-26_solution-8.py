from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num
	Do not include these tokens in the code: unique
	"""
    # YOUR CODE HERE

    num = len(numbers)
    unique = list(range(num))
    unique_count = 0

    for i in range(num):
        for j in range(i+1, num):
            if numbers[i] == numbers[j]:
                break
        else:
            unique[unique_count] = numbers[i]
            unique_count += 1

    return unique


def fibonacci(n):
    if n == 1:
        return [1, 1]
    else:
        res = fibonacci(n - 1)
        return [res[-1], res[-1] + res[-2]]


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4]
    # Should be [1, 3, 4]
    removal = remove_duplicates(numbers)
    print(removal)

    fib_len = int(input("Input for number of Fibonacci numbers to return: "))
    fibs = fibonacci(fib_len)
    print(fibs)
