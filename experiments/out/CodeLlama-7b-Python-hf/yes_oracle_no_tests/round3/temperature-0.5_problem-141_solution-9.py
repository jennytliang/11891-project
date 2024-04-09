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

 
    if len(file_name) > 8:
        return 'No'
    else:
        if file_name.count('.') == 1:
            if file_name.rfind('.') > 4:
                return 'No'
            else:
                if file_name[file_name.find('.') + 1] in ('txt', 'exe', 'dll'):
                    return 'Yes'
                else:
                    return 'No'
        else:
            return 'No'
 
 
if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))
 
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("WebSite.com") == "No"
    assert file_name_check("start.html") == "Yes"
    assert file_name_check("index.html") == "Yes"
    assert file_name_check("empty.") == "No"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.DLL") == "No"
    assert file_name_check("com.exe") == "Yes"
    assert file_name_check("123.exe") == "No"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("Website.COM") == "No"
    assert file_name_check("123") == "No"
    assert file_name_check("123.") == "No"
    assert file_name_check("123.exe.exe") == "No"
    assert file_name_check("Website.COM.exe") == "No"
    assert file_name_check("123.exe.dll") == "No"
    assert file_name_check("Website.COM.dll") == "No"
    assert file_name_check("123.