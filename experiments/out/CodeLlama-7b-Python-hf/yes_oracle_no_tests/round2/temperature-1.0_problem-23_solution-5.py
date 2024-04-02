def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur : int
    count : int
    letter : str

    count = 0
    for letter in string :
        count = count + 1
    return count

print("strlen('')==0:", strlen('')==0)
print("strlen('abc')==3:", strlen('abc')==3)
