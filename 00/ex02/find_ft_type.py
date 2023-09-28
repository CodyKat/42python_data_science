def all_thing_is_obj(object: any) -> int:
    typename = type(object).__name__
    typename = typename.capitalize()
    if (typename == "Str"):
        print("{} is in the kitchen : {}".format(object, type(object)))
    elif (typename == "Int"):
        print("Type not found")
    else:
        print("{} : {}".format(typename, type(object)))
    return 42