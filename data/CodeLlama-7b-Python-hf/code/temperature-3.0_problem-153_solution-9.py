def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    # Please print out which test case you're currently on (for example, "Test Case #2")
    # print("#1")
    
    # Add your code here
  
    # print(class_name)
    strongest_list = []
    
    for item in extensions:
        cap = 0
        sm = 0
        for i in item:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                cap += 1
            elif i in "abcdefghijklmnopqrstuvwxyz":
                sm += 1
        
        strength = cap-sm
        strongest_list.append((strength,item))
        #print(item, strength)
        
    strongest = max(strongest_list)
    print(strongest[1])
    # strongest_extension = []
    # strongest_list = sorted(strongest_list)
    # max_strength = strongest_list[len(strongest_list)-1][0]
    # print(strongest_list)
    # print(max_strength)
    # for i in strongest_list:
    #     if i[0] == max_strength:
    #         strongest_extension.append(i)
    #         print(i[1])
    #         break
    
    return f'{class_name}.{strongest[1]}'






if __name__ == '__main__':
    #print(strongestExtension("a", ["AA", "Be", "CC"]))  # == "a.AA"
    # #print(strongestExtension('my_class', ['AA', 'Be', 'CC']))  # == 'my_class.AA'
    # print(strongestExtension('test_class', ["ta"," tg","   tt","t"]))  # == 't'