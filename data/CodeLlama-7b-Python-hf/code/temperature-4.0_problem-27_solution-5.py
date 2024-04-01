def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # result = ''
    # for s in range(len(string)):
    #     if 0 < ord(string[s]) <= 122:
    #         # 0123 - 097
    #         result += char(96 + (097 - ord(string[s]) - 5))+char(str(string[s]) + 47)
    #         continue
    # for s1 in range(len(string))):
    #     if string[s - 1].islower() ):
    #         result+ = str(string)[s-1] ^ 64    

    result = ''
    for s in range(len(string)):
        result+= chr(((64-(ord((string[s]))&63)))^65)

    