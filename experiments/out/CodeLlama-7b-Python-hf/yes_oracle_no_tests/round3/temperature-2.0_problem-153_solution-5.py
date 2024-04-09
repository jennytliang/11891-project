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
    class_name = class_name
    extensions = extensions
    # Your code here
    strongest_extension = extensions[0]
    strongest_extension_strength = strength(extensions[0])

    for extension in extensions:
        if strength(extension) > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength(extension)

    return class_name + '.' + strongest_extension


def strength(s):
    return len([i for i in s if i.isupper()]) - len([i for i in s if i.islower()])


# Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
# Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])
# Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
# Strongest_Extension('my_class', ['AA', 'aB', 'cC'])
# Strongest_Extension('my_class', ['a', 'b', 'c'])
# Strongest_Extension('my_class', ['A', 'B', 'C'])




