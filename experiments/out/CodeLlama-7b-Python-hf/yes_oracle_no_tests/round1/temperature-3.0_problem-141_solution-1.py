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
    return 'Yes' if file_name.count('.') == 1 and file_name.count('0') <= 3 and file_name.split('.')[0].isalpha() and file_name.split('.')[1] in ['txt', 'exe', 'dll'] else 'No'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("") == 'No', "Empty"
    assert file_name_check("1.exe") == 'No', "Wrong2"
    assert file_name_check("txt.exe") == 'No', "Wrong3"
    assert file_name_check("t.exe") == 'No', "Wrong4"
    assert file_name_check("1.exe") == 'No', "Wrong5"
    assert file_name_check("folder.exe") == 'No', "Wrong6"
    assert file_name_check("f.txt") == 'Yes', "Txt1"
    assert file_name_check("folder.dll") == 'Yes', "Wrong7"
    assert file_name_check("filename.txt") == 'Yes', "Txt2"
    assert file_name_check("filename.dll") == 'Yes', "dll1"
    assert file_name_check("filename.exe") == 'Yes', "exe1"
    assert file_name_check("filename.TxT") == 'No', "Wrong8"
    assert file_name_check("folder1.dll") == 'Yes', "dll2"
    assert file_name_check("folder1.TXT") == 'No', "Wrong9"
    assert file_name_check("filename.txt") == 'Yes', "Txt3"
    assert file_name_check("filename.txt") == 'Yes', "Txt4"
    assert file_name_check("folder1.exe") == 'Yes', "exe2"
    assert file_name_check("folder2.txt") == 'Yes', "Txt5"
    assert file_