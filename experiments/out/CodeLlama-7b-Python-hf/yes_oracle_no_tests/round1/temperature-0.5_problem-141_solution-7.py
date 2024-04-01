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

    if file_name.count(".") != 1:
        return "No"

    if not file_name[:file_name.find(".")].isalpha():
        return "No"

    if file_name[file_name.find(".") + 1 :].lower() not in ["txt", "exe", "dll"]:
        return "No"

    if len(file_name) - len(file_name.replace("0123456789", "")) > 3:
        return "No"

    return "Yes"


def test_function():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.dll") == "Yes"
    assert file_name_check("example.tar.gz") == "Yes"
    assert file_name_check("example.tar.xz") == "Yes"
    assert file_name_check("example.tar.bz2") == "Yes"
    assert file_name_check("example.2txt") == "Yes"
    assert file_name_check("example.2exe") == "Yes"
    assert file_name_check("example.2dll") == "Yes"
    assert file_name_check("example.txt.2") == "No"
    assert file_name_check("example.exe.2") == "No"
    assert file_name_check("example.dll.2") == "No"
    assert file_name_check("example.tar.gz.2") == "No"
    assert file_name_check("example.tar.xz.2") == "No"
    assert file_name_check("example.tar.bz2.2") == "No"
    assert file_name_check("example.tar.gz.txt") == "No"
    assert file_name_check("example.tar.xz.exe") == "No"
    assert file_name_check("example.tar.bz2.dll") == "No"
    assert file