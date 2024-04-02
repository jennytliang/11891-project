def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    # Write your code here
    m = [" I ", " V ", " X ", " L ", " C ", " D ", " M "]
    n = number
    if not 0 < number <= 1000:
        raise ValueError("Romans only go up to mmm.")
    result = []
    c = 1
    while n:
        d, n = divmod(n, 10)
        result.append((m[n - 1]) * n)
        if d > 5:
            result.append(m[c + 4])
        elif d >= 5:
            result.append(m[c] + m[c + 1])
        elif d == 5:
            result.append(m[c + 4])
        c += 2
    return "".join(result).replace(" ", "")

if __name__ == "__main__":
    num = int(input().strip())
    print(int_to_mini_roman(num))