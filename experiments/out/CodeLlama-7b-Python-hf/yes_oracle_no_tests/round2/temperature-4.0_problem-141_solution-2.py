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
    
	Do not include these tokens in the code: # your code here
	"""
    return 'Yes' if file_name.count('.') == 1 and file_name.count('0') <= 3 and file_name.count('9') <= 3 and file_name.split('.')[1] in ['txt','exe','dll'] and file_name.split('.')[0][0] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] else 'No'

if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.dll") == "Yes"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("e7example.txt") == "No"
    assert file_name_check("e7.txt") == "No"
    assert file_name_check("example.t") == "No"
    assert file_name_check("examplec.txt") == "No"
    assert file_name_check("example.exe.txt") == "No"
    assert file_name_check("example.exe.exe") == "No"
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
