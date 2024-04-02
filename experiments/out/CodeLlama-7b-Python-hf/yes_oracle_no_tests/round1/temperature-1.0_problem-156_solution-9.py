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
    m = ["I", "V", "X", "L", "C", "D", "M"]
    s = []
    i = 0
    while number > 0:
        if number >= 1000:
            s.append(m[i])
            number -= 1000
        elif number >= 500:
            s.append(m[i])
            number -= 500
        elif number >= 100:
            s.append(m[i])
            number -= 100
        elif number >= 50:
            s.append(m[i + 1])
            number -= 50
        elif number >= 10:
            s.append(m[i])
            number -= 10
        elif number >= 5:
            s.append(m[i + 1])
            number -= 5
        elif number >= 1:
            s.append(m[i])
            number -= 1
        i += 1
    s.reverse()
    return "".join(s)



def main():
    number = 19
    print(int_to_mini_roman(number))


if __name__ == "__main__":
    main()
