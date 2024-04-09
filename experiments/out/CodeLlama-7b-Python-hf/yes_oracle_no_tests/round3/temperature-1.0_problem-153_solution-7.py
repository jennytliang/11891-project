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
    strongest_extension = extensions[0]
    strongest_extension_strength = -1
    for extension in extensions:
        strength = strength_of_extension(extension)
        if strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength
    return f'{class_name}.{strongest_extension}'


def strength_of_extension(extension):
    cap_count = 0
    sm_count = 0
    for char in extension:
        if char.isupper():
            cap_count += 1
        elif char.islower():
            sm_count += 1
    return cap_count - sm_count


def Strongest_Extension_2(class_name, extensions):
    return class_name + "." + max(extensions, key=strength_of_extension)
