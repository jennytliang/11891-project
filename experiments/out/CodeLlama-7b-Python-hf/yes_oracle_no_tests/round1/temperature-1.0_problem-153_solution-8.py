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
    
	Include these tokens in the code: def strength ( s : str ) -> int :
	"""
    
    # get the longest class name to adjust indexing accordingly within the function
    maxi = len(class_name) - 1
    # initialize a strength variable and find the strongest extension
    s_strength = 0
    s_ext_name = ' '
    s_ext_index = 0
    for i in range(len(extensions)):
        strength = 0
        # get the lowercase letters in an extension name
        num_sm = 0
        for j in range(len(extensions[i])):
            char = extensions[i][j].lower()
            if ord(char) >= 97 and ord(char) <= 122:
                num_sm += 1
        
        # find the uppercase letters in an extension name
        upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num_cap = 0
        for char in extensions[i]:
            if (ord(char) >= 65 and ord(char) <= 90) or (char in upper_char):
                num_cap += 1  # uppercase letter
        # set a strength score as num_cap - num_sm
        strength = num_cap - num_sm
        # update the strongest extension, strength score, and index accordingly
        if s_strength < strength:
            s_strength = strength
            s_ext_name = extensions[i]
            s_ext_index = i
        
    return class_name + '\'' + s_ext_name

    # return class_name, s_ext_name

print(Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]))
print(Strongest_Extension("Gloves", ["DexGloves", "Thorloves", "Gutloves", "Waterloves"]))
