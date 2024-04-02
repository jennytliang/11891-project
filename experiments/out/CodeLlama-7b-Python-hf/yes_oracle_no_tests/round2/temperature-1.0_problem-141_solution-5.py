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
	Do not include these tokens in the code: def
	"""
    file_name_lc=file_name.lower()
    x=file_name_lc.split(".",1)
    t=x[1] if len(x)>1 else ["dummy"]
    x=[x[0],t[0],x[1]] if len(x)>1 else [x[0],"dummy","dummy"]

    x=[i for i in x[0] if i.isdigit()]

    ans="Yes" if len(x)<=3 else "No"

    ans="Yes" if x[0].isalpha() and len(x)<10 and len(x[0])>0 and i[1] in ["txt","exe","dll"] else "No"

    return ans
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.dll.exe")) # => 'No' (Too many characters after the period)
print(file_name_check("aa.ex")) # => 'No' (Too few characters after the period)
print(file_name_check("example.dll.h")) # => 'No' (Invalid file extension) 