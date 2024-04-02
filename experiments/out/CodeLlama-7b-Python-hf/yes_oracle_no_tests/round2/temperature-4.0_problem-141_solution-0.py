def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    
	Include these tokens in the code: len ( list ( filter ( lambda ch : ch
	"""

  # Please, insert your code here

    if file_name.count(".") != 1:
        return "No"

    if len(file_name) == 0:
        return "No"

    if file_name.count("") != 0:
        return "No"

    if file_name.count(" ") != 0:
        return "No"

    if file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
        return "No"

    if file_name[0].isdigit() == True:
        return "No"

    if file_name[-4:] != ".txt" and file_name[-4:] != ".exe" and file_name[-4:] != ".dll":
        return "No"

    return "Yes"


print("Example:")
print(file_name_check("example.txt"))

# These "asserts" are used for self-checking and not for an auto-testing
assert file_name_check("example.txt") == "Yes"
assert file_name_check("x1.dll") == "No"
assert file_name_check("i.am.txt") == "No"
assert file_name_check("1.exe") == "No"
assert file_name_check(".dll") == "No"
assert file_name_check("code. C") == "No"
print("Coding complete? Click 'Check' to earn cool rewards!")
