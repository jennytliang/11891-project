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
    
	Include these tokens in the code: if len ( list ( filter ( lambda
	Do not include these tokens in the code: count _ digit = 0
	"""
    if file_name.count(".") > 1:
        return "No"
    if file_name.count(".") == 1:
        if file_name.count("a") == 0 and file_name.count("A") == 0:
            return "No"
        if file_name.count("0") == 0 and file_name.count("1") == 0 and file_name.count("2") == 0 and file_name.count("3") == 0 and file_name.count("4") == 0 and file_name.count("5") == 0 and file_name.count("6") == 0 and file_name.count("7") == 0 and file_name.count("8") == 0 and file_name.count("9") == 0:
            return "Yes"
        else:
            return "No"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("example.txt") == "Yes", "First"
    assert file_name_check("example.exe") == "Yes", "Second"
    assert file_name_check("long_file.dll") == "Yes", "Third"
    assert file_name_check("two on one.dll") == "No", "Fourth"
    assert file_name_check("1example.txt") == "No", "Fifth"
    assert file_name_check("-.exe") == "No", "Sixth"
    assert file_name_check("-example.txt") == "No", "Seventh"
    assert file_name_check("a-.txt") == "No", "Eighth"
    assert file_name_check("a-b.txt") == "Yes", "Ninth"
    assert file_name_check("1.dll") == "No", "Tenth"
    assert file_name_check("t.u") == "No", "Eleventh"
    assert file_name_check("a.c") == "Yes",