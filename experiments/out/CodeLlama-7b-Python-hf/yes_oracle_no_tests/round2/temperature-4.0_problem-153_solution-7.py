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
    
	Include these tokens in the code: def strength
	Do not include these tokens in the code: if len
	"""
    strongest_extension = extensions[0]
    strongest_extension_strength = strength(strongest_extension)
    
    for extension in extensions:
        strength_of_extension = strength(extension)
        if strength_of_extension > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength_of_extension
        
    return class_name + '.' + strongest_extension

def strength(extension):
    return len(extension) - len(extension.lower())

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))