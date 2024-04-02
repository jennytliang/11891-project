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
	Do not include these tokens in the code: # write your code here
	"""
    return 'Yes' if len(list(filter(lambda ch: ch.isdigit(), file_name))) <= 3 and file_name.count('.') == 1 and file_name.split('.')[-1] in ['txt', 'exe', 'dll'] else 'No'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert file_name_check("1.txt") == 'No', "1st example"
    assert file_name_check("example.txt") == 'Yes', "2nd example"
    assert file_name_check("exampl.e.txt") == 'No', "3rd example"
    assert file_name_check("example.t") == 'No', "4th example"
    assert file_name_check("example.tex") == 'No', "5th example"
    assert file_name_check("example.") == 'No', "6th example"
    assert file_name_check("example.d") == 'No', "7th example"
    assert file_name_check("example.td") == 'No', "8th example"
    assert file_name_check("example.dll") == 'Yes', "9th example"
    assert file_name_check("example.DL") == 'No', "10th example"
    assert file_name_check("example.DL") == 'No', "11th example"
    assert file_name_check("example.dL") == 'No', "12th example"
    assert file_name_check("example.T") == 'No', "13th example"
    assert file_name_check("example.t") == 'No', "14th example"
    assert file_name_check("example.e") == 'No', "15th example"
    assert file_name_check("example.E") == 'No', "16th example"
    assert file_name_check("example.") == 'No', "17th example"
    assert file_name_check("example") == 'No', "18