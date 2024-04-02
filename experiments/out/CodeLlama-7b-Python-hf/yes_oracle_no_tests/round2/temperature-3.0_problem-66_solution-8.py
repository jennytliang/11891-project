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

    # First, we'll convert the input string into a list, where each element is a character. Use the split() function.
    string_list = s.split()
    # Next, we'll create a new list that will contain only the upper characters.
    upper_chars = []
    for char in string_list:
        if char.isupper():
            upper_chars.append(char)
    # Now, we'll create a new variable that will contain the sum of the ASCII codes of the characters in the upper_chars list.
    sum = 0
    for char in upper_chars:
        sum += ord(char)
    return sum


print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))
