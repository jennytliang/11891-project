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
    class_name_list = []
    class_name_list.append(class_name)
    strongest_extension = ''
    strongest_extension_name = ''
    count = 0
    flag = True
    for extension in extensions:
        extension_name = extension
        extension_name_upper_count = 0
        extension_name_lower_count = 0
        for i in extension:
            if i.isupper():
                extension_name_upper_count += 1
            elif i.islower():
                extension_name_lower_count += 1
        fraction = extension_name_upper_count - extension_name_lower_count
        if flag:
            count = fraction
            strongest_extension_name = extension_name
            flag = False
        elif count < fraction:
            count = fraction
            strongest_extension_name = extension_name
    strongest_extension = ' '.join(class_name_list) + '.' + strongest_extension_name
    return strongest_extension