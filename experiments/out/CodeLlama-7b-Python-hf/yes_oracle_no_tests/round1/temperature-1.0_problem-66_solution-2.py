def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
	Include these tokens in the code: return
	"""
    # First, I create a list of the upper characters
    upper_characters = []
    for character in s:
        if character.isupper():
            upper_characters.append(character)

    # I then create a list of the ASCII codes of the upper characters
    ascii_codes = []
    for character in upper_characters:
        ascii_codes.append(ord(character))

    # I then sum the list
    sum_ascii_codes = sum(ascii_codes)

    return sum_ascii_codes


if __name__ == '__main__':
    print(digitSum(""))
    print(digitSum("abAB"))
    print(digitSum("abcCd"))
    print(digitSum("helloE"))
    print(digitSum("woArBld"))
    print(digitSum("aAaaaXa"))
