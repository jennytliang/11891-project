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
    """
    
    digit = lambda x: x in '123456789O'
    digit_dict ={1:0}
    letter = lambda x: x in 'ABCDEFGHIKLMNOPQRDSTUVWYZabcdefghjklmnopqdrstuyz'   # wrong j
    alphabet = letter | digit  # wrong k
                              
                             
    name, name_list=  file_name.translate(None, '.' ), [] # 1.
                                #for i in  file_name: 
                                   # if i=='.' or digit(i):# if digit(x): 
                                    #   print  'True'
    name =name.split(name)
    if len(name)>=2:
            print 'yes'
            for x in name[int(name.find("."))]:                         # 2. 
               if not(letter(x)):   # or not x                       # 9. check x is a digit or not using builtin func 
                     return
            return 'No'
           else:
               return 'No'
           return

             
print file_name