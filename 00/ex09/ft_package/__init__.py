def count_in_list(object: list, to_find: any) -> int:
    count = 0
    for i in object:
        if i == to_find:
            count += 1
    return count


count_in_list.__doc__ = """count how many to_find in object"""
