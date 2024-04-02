def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s = str ( x )
	"""

    s = str(x)

    if len(s) - shift < 0:
        return s[shift:-shift] + s[:shift]
    else:
        return s[shift:] + s[:shift]

        
def main():
    import doctest
    doctest.testmod()
    print(circular_shift(12, 2))

if __name__ == "__main__":
    main()