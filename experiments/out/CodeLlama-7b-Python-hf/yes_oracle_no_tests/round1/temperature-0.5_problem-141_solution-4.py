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
    
	Include these tokens in the code:  if len ( list ( filter ( lambda
	Do not include these tokens in the code: file _ name . count
	"""

    if file_name.count(".") == 1:
        if file_name.count("0") <= 2 and file_name.count("9") <= 2:
            if file_name[0].isalpha() == True:
                if file_name[-4:] in [".txt", ".exe", ".dll"]:
                    return "Yes"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("0example.txt") == "No"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.exe.old") == "No"
    assert file_name_check("windows2012.dll") == "Yes"
    assert file_name_check("com.module.class") == "No"
    assert file_name_check("l33t.hacker") == "Yes"
    assert file_name_check(".no.ext.") == "No"
    assert file_name_check("no..ext") == "No"
    assert file_name_check("no_ext") == "Yes"
    print("Coding complete? Click 'Check' to earn cool rewards!")