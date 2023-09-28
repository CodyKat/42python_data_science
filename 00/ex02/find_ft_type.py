def all_thing_is_obj(object: any) -> int:
    typename = type(object).__name__
    typename = typename.capitalize()
    if typename == 'List' or typename == 'Tuple' or \
        typename == 'Set' or typename == 'Dict':
        print("{} : {}".format(typename, type(object)))
    elif typename == "Str":
        print("{} is in the kitchen : {}".format(object, type(object)))
    else:
        print("Type not found")
    return 42