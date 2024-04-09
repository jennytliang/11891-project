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
    
	Include these tokens in the code: if len ( list ( filter ( lambda ch :
	"""
    # your code here
    import re
    # print(file_name)
    if file_name.count(".") == 1 and file_name.count(" ") == 0:
        if file_name.count("0") <= 3 and file_name.count("1") <= 3 and file_name.count("2") <= 3 and file_name.count("3") <= 3 and file_name.count("4") <= 3 and file_name.count("5") <= 3 and file_name.count("6") <= 3 and file_name.count("7") <= 3 and file_name.count("8") <= 3 and file_name.count("9") <= 3:
            if file_name.split(".")[1] in ["txt", "exe", "dll"]:
                return "Yes"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("screen.ini") == "No", "1st example"
    assert file_name_check("l33t.exe") == "No", "2nd example"
    assert file_name_check("hello.dll") == "Yes", "3rd example"
    assert file_name_check("A.b.c.d.exe") == "No", "4th example"
    assert file_name_check("README.md") == "Yes", "5th example"
    assert file_name_check("Humans.txt") == "Yes", "6th example"
    assert file_name_check("json.txt") == "No", "7th example"
    assert file_name_check("def.exe") == "No", "8th example"
