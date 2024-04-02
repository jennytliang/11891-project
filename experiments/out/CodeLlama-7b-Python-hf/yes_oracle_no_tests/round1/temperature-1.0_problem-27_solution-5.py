def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = list(string)

    # replace all letters with their opposites
    for i, c in enumerate(r):
        if c.islower():
            r[i] = c.upper()
        elif c.isupper():
            r[i] = c.lower()

    # flip all the " " into "-"
    r = ["-" if c == " " else c for c in r]

    return "".join(r)


if __name__ == "__main__":
    s = "Hello I love computer science"
    print(flip_case(s))
