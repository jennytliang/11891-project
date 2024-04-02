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
    max_strength = 0
    strongest_extension = ""
    for extension in extensions:
        strength = strength_of_extension(extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension


def strength_of_extension(extension):
    cap = 0
    sm = 0
    for letter in extension:
        if letter.isupper():
            cap += 1
        elif letter.islower():
            sm += 1
    return cap - sm


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('compiler', ['compiler', 'Compiler', 'COMPILER']) == 'compiler.compiler'
    assert Strongest_Extension('z', ['a', 'aa', 'aaa']) == 'z.a'
    assert Strongest_Extension('z', ['', 'a', 'aa', 'aaa']) == 'z.a'
    assert Strongest_Extension('z', ['', 'a', 'aa']) == 'z.a'
    assert Strongest_Extension('webServer', ['web', 'WebServer', 'webserver']) == 'webServer.WebServer'
    assert Strongest_Extension('webServer', ['web', 'Web', 'webserver']) == 'webServer.Web'
    assert Strongest_Extension('webServer', ['web', 'Web', 'WebServer']) == 'webServer.WebServer'
    print("Coding complete? Click 'Check' to earn cool rewards!")
