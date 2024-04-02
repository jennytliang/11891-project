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

  # Please, insert your code here:  
def file_name_check(file_name):    
    count = 0          
    index = file_name.find(".txt")  
          
    for i in range(len(file_name)):          
        if file_name[i].isdigit():               
            count += 1          

    if count <= 3 and index != - 1 and file_name[0].isalpha() == True and\
        (file_name.find(".exe",index) != - 1 or file_name.find(".dll",index) != - 1):
        result = 'Yes'
    else:
        result = 'No'
          
    return result

# Please, insert your code in one or more files, until all the above function are complete
# (remember that you can use the 'import PythonFile' sentence, if all the above function were
# included in the same file)    

# Please, check the following code before to submit (this is just a sample):
file_name = '1example.exe'

# Do not modify the following code (it could be useful if you want to test your code):
print("{0} => {1}".format(file_name, file_name_check(file_name)))