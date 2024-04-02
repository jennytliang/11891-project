def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0
    for ch in str(num):
        if ch == '0':
            odd += 1
        else:
            even += 1
    return even, odd


def main():
    print(even_odd_count(12345))
    print(even_odd_count(123456789))


if __name__ == "__main__":
    main()
