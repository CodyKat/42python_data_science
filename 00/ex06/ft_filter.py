def ft_filter(function, iterable) -> object:
    ret = [i for i in iterable if function(i) is True]
    for i in ret:
        yield i


ft_filter.__doc__ = """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
