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
    # your code here
    strongest_extension = ''
    strongest_extension_strength = 0
    for extension in extensions:
        extension_strength = 0
        for letter in extension:
            if letter.isupper():
                extension_strength += 1
            elif letter.islower():
                extension_strength -= 1
        if extension_strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = extension_strength
    return class_name + '.' + strongest_extension


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('My_Class', ['aA', 'Be', 'CC']) == 'My_Class.aA'
    assert Strongest_Extension('My__Class', ['aA', 'Be', 'CC']) == 'My__Class.Be'
    assert Strongest_Extension('My_Clas', ['aA', 'Be', 'CC']) == 'My_Clas.aA'
    print("Coding complete? Click 'Check' to earn cool rewards!")