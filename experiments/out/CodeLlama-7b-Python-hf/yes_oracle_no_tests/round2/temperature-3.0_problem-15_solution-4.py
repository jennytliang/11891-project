def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in range(n + 1):
        r += str(i)
        r += " "
    return r[:-1]

    # r = ""
    # for i in range(n + 1):
    #     r += str(i)
    #     r += " "
    # return r

    # return " ".join(str(i) for i in range(n + 1))

    # return " ".join(str(i) for i in range(n + 1))




def main():
    try:
        print(string_sequence(int(input("Enter a number: "))))
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
