def all_thing_is_obj(object: any) -> int:
    typename = type(object).__name__
    typename = typename.capitalize()
    if typename == 'List' or typename == 'Tuple' or \
        typename == 'Set' or typename == 'Dict':
        print(f"{typename} : {type(object)}")
    elif typename == "Str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42