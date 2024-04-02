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

  # Please, insert your code here.

    if file_name.count(".") == 1 and file_name.count("0") <= 3 and file_name.count("9") <= 3:
        if file_name.count(".") == 1:
            if file_name.find(".") != len(file_name) - 4:
                if file_name.find(".") != 0:
                    if file_name.find(".") == 1:
                        if file_name.find(".") == 2:
                            if file_name.find(".") == 3:
                                if file_name.split(".")[0][0].isalpha() == True:
                                    if file_name.split(".")[1] == "txt" or file_name.split(".")[1] == "exe" or file_name.split(".")[1] == "dll":
                                        return "Yes"
                                    else:
                                        return "No"
                                else:
                                    return "No"
                            else:
                                return "No"
                        else:
                            return "No"
                    else:
                        return "No"
                else:
                    return "No"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.txt"))
print(file_name_check("example.tar.gz"))
print(file_name_check("example.tar.bz2"))
print(file_name_check("example.tar.xz"))
print(file_name_check("example.tar.7z"))
print(file_name_check("example.tar.bak"))
print(file_name_check("example.tar.txt"))