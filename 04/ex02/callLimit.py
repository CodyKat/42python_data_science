def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count == limit:
                print('Error: <function {} at {}> call too many times'.format(function.__name__, hex(id(function))))
            else:
                function()
                count += 1
        return limit_function
    return callLimiter