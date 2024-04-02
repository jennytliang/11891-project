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

    strongest_extension = ""
    strength = 0
    strongest_extension_name = ""
    
    for extension in extensions:
        CAP = 0
        SM = 0
        new_strength = 0
        for character in extension:
            if ord(character) >= 65:
                CAP += 1
            elif ord(character) <= 122:
                SM += 1
        new_strength = CAP - SM
        if new_strength > strength:
            strength = new_strength
            strongest_extension = extension
    
    return f'{class_name}.{strongest_extension}'

if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
    print(Strongest_Extension('my_class', ['AA', 'CC']))
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA', 'First'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.Be', 'Second'
    assert Strongest_Extension('my_class', ['AA', 'CCCC', 'DP']) == 'my_class.DP', 'Third'
    print("Coding complete? Click 'Check' to earn cool rewards!")
