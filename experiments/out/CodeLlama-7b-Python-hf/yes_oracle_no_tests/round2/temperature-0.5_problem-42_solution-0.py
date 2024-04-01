def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Do not include these tokens in the code: def inc r _ list 2 ( l :
	"""


    return [x + 1 for x i l]


def main():
    # Test your code with this first
    x = [1, 2, 3]
    print(incr_list(x))

    # After you are satisfied with your results, use input() to prompt the user
    # for a string and try your function with that input.
    # user_string = input('Enter a string: ')
    # print(reverse_string(user_string))


if __name__ == '__main__':
    main()