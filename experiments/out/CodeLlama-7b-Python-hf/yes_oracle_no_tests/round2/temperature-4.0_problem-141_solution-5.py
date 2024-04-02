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

  # Please, insert here your code


  # Please, do not modify the code below

if __name__ == '__main__':
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("example.dll") == 'Yes'
    assert file_name_check("example.txt.bak") == 'No'
    assert file_name_check("example.dll.bak") == 'No'
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("example.exe.bak") == 'No'
    assert file_name_check("example.dll.exe") == 'No'
    assert file_name_check("1example.txt.exe") == 'No'
    assert file_name_check("example.txt.exe") == 'Yes'
    assert file_name_check("example.exe.dll") == 'Yes'
    assert file_name_check("example.txt.dll") == 'Yes'
    assert file_name_check("example.dll.txt") == 'Yes'
    assert file_name_check("1example.dll.exe") == 'No'
    assert file_name_check("example.exe.bak.dll") == 'No'
    assert file_name_check("example.dll.bak.exe") == 'No'
    assert file_name_check("1example.exe.bak.dll") == 'No'
    assert file_name_check("1example.dll.bak.exe") == 'No'
    assert file_name_check("1example.exe.bak.txt") == 'No'
    assert file_name_check("1example.dll.bak.txt") == 'No'
    assert file_name_check("1example.dll.exe.bak") == 'No'
    assert file_name_check("example.exe.bak.txt") == 'Yes'
    assert file_name_check("example.dll.bak.txt") == 'Yes'
