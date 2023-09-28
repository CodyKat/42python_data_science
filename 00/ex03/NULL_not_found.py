def NULL_not_found(object: any) -> int:
    typeinfo = type(object)
    typename = typeinfo.__name__
    if typename == "NoneType":
        print("Nothing: {} {}".format(object, typeinfo))
    elif typename == "int":
        print("Zero: {} {}".format(object, typeinfo))
    elif typename == "float":
        print("Cheese: {} {}".format(object, typeinfo))
    elif typename == "str" and object == '':
        print("Empty: {} {}".format(object, typeinfo))
    elif typename == "bool":
        print("Fake: {} {}".format(object, typeinfo))
    else:
        print("Type not Found")
        return 1
    return 0
