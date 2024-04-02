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
    #First we extract the uppercase letters in the extension's name
    #and the lowercase letters in the extension's name
    uppercase = 0
    lowercase = 0
    for i in range(len(extensions[0])):
        if extensions[0][i].isupper():
            uppercase += 1
        if extensions[0][i].islower():
            lowercase += 1
    #We calculate the strength of the extension
    strength = uppercase - lowercase
    #We define the extension with the highest strength
    max_strength = strength
    #We define the extension with the highest strength
    strongest_extension = extensions[0]
    #We iterate through the extensions and compare the strength
    for i in range(len(extensions)):
        uppercase = 0
        lowercase = 0
        for j in range(len(extensions[i])):
            if extensions[i][j].isupper():
                uppercase += 1
            if extensions[i][j].islower():
                lowercase += 1
        strength = uppercase - lowercase
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extensions[i]
    #We return the extension with the highest strength
    return class_name + "." + strongest_extension

























