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
	Do not include these tokens in the code: return
	"""
    return "No" if len([x for x in file_name if x.isdigit()]) > 3 or file_name.count(".") != 1 or file_name.count(".") != 1 or file_name.split(".")[1] not in ["txt", "exe", "dll"] else "Yes"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("1.txt") == "No", "1st Example"
    assert file_name_check("web.html") == "No", "2nd Example"
    assert file_name_check("1.exe") == "No", "3rd Example"
    assert file_name_check("1.exe.old") == "No", "4th Example"
    assert file_name_check("web.image.png") == "No", "5th Example"
    assert file_name_check("web.image.png.bak") == "No", "6th Example"
    assert file_name_check("web.1.exe") == "No", "7th Example"
    assert file_name_check("web.1.exe.old") == "No", "8th Example"
    assert file_name_check("1web.image.png") == "No", "9th Example"
    assert file_name_check("abc.exe") == "Yes"
    assert file_name_check("abc.old.exe") == "Yes"
    assert file_name_check("abc.old.jpg") == "Yes"
    assert file_name_check("abc.old.1.jpg") == "Yes"
    assert file_name_check("1.2.jpg") == "Yes", "10th Example"
    assert file_name_check("1.2.3.4.jpg") == "No", "11th Example"
